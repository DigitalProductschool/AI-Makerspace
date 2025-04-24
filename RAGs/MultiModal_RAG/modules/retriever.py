"""
Retriever module using Qdrant for semantic search on text and image embeddings.
Supports indexing and RAG-style multimodal retrieval for a given document.
"""

import os
import io
import uuid
import base64
import numpy as np
from pathlib import Path
from typing import List, Tuple, Optional
from PIL import Image

import streamlit as st
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct, Filter

from modules.utils import safe_log
from modules.config import OPENAI_API_KEY
from modules.embedding_utils import embed_text, embed_image, embed_query_for_image_search
from modules.llm_respond import generate_rag_caption

# --- Constants ---
QDRANT_PATH = Path("data/qdrant_db").resolve()
TEXT_COLLECTION = "text_embeddings"
IMAGE_COLLECTION = "image_embeddings"

QDRANT_PATH.mkdir(parents=True, exist_ok=True)

# --- Qdrant Initialization ---
@st.cache_resource(show_spinner=False)
def get_qdrant() -> QdrantClient:
    """Initialize and return a Qdrant client with the necessary collections."""
    qdrant = QdrantClient(path=str(QDRANT_PATH))

    if not qdrant.collection_exists(TEXT_COLLECTION):
        qdrant.create_collection(
            collection_name=TEXT_COLLECTION,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
        )

    if not qdrant.collection_exists(IMAGE_COLLECTION):
        qdrant.create_collection(
            collection_name=IMAGE_COLLECTION,
            vectors_config=VectorParams(size=512, distance=Distance.COSINE)
        )

    return qdrant

# --- Indexing ---
def index_chunks(doc_id: str, text_chunks: List[dict]) -> None:
    """Indexes a list of text chunks into Qdrant."""
    qdrant = get_qdrant()
    points = []

    for chunk in text_chunks:
        text = chunk.get("text", "").strip()
        if not text:
            continue
        embedding = embed_text(text)
        points.append(PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={
                "doc_id": doc_id,
                "chunk": text,
                "page": chunk.get("page"),
                "source": chunk.get("source"),
                "type": "text",
            }
        ))

    qdrant.upsert(collection_name=TEXT_COLLECTION, points=points)
    safe_log(f"📚 Indexed {len(points)} text chunks into Qdrant.")

def index_images(doc_id: str, image_list: List[dict]) -> None:
    """Indexes images with optional captions into Qdrant."""
    qdrant = get_qdrant()
    points = []

    for idx, img in enumerate(image_list):
        try:
            embedding = embed_image(img["image_bytes"])
            caption = img.get("caption", "")
            caption_emb = embed_text(caption) if caption else None

            image_b64 = base64.b64encode(img["image_bytes"]).decode("utf-8")

            points.append(PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "doc_id": doc_id,
                    "caption": caption,
                    "page": img.get("page"),
                    "order_idx": idx,
                    "image_b64": image_b64,
                    "caption_embedding": caption_emb.tolist() if caption_emb is not None else None,
                    "type": "image"
                }
            ))
        except Exception as e:
            safe_log(f"⚠️ Failed to index image {idx + 1}: {e}")

    if points:
        qdrant.upsert(collection_name=IMAGE_COLLECTION, points=points)
        safe_log(f"🖼️ Indexed {len(points)} images into Qdrant.")
    else:
        safe_log("⚠️ No images were indexed.")

# --- Retrieval ---
def get_relevant_content(doc_id: str, query: str) -> Tuple[str, Optional[List[dict]], Optional[List[str]]]:
    """
    Retrieves the most relevant text and images for a given query from Qdrant.

    Returns:
        Tuple of (best text chunk, relevant images with metadata, RAG-style captions).
    """
    qdrant = get_qdrant()

    # Text retrieval
    text_vec = embed_text(query)
    text_hits = qdrant.query_points(
        collection_name=TEXT_COLLECTION,
        query=text_vec,
        limit=5,
        with_payload=True,
        query_filter=Filter(must=[{"key": "doc_id", "match": {"value": doc_id}}])
    )
    best_text = text_hits.points[0].payload["chunk"] if text_hits.points else ""

    # Image retrieval
    image_vec = embed_query_for_image_search(query)
    image_hits = qdrant.query_points(
        collection_name=IMAGE_COLLECTION,
        query=image_vec,
        limit=10,
        with_payload=True,
        query_filter=Filter(must=[{"key": "doc_id", "match": {"value": doc_id}}])
    )

    top_images = []
    for hit in image_hits.points:
        payload = hit.payload
        payload["score"] = hit.score
        top_images.append(payload)

    # Generate captions (RAG-style)
    rag_captions = []
    for img in top_images:
        if img and "image_b64" in img:
            rag_caption = generate_rag_caption(
                base64.b64decode(img["image_b64"]),
                query=query,
                context=best_text
            )
        else:
            rag_caption = None
        rag_captions.append(rag_caption)

    return best_text, top_images, rag_captions

def get_all_chunks(doc_id: str) -> str:
    """
    Retrieves all text chunks for a given document ID.

    Returns:
        str: Combined text content.
    """
    qdrant = get_qdrant()
    all_points, _ = qdrant.scroll(
        collection_name=TEXT_COLLECTION,
        scroll_filter=Filter(must=[{"key": "doc_id", "match": {"value": doc_id}}]),
        with_payload=True,
        limit=500
    )
    chunks = [pt.payload["chunk"] for pt in all_points]
    safe_log(f"📚 Retrieved {len(chunks)} total chunks for doc_id: {doc_id}")
    return "\n".join(chunks)