"""
Embedding utility functions for text and image similarity tasks.
Supports both OpenAI embeddings and CLIP-based embeddings.
"""

import io
import numpy as np
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
import openai
from openai import OpenAI
from modules.config import OPENAI_API_KEY


# -------------------------
# --- Initialization ---
# -------------------------

# Set OpenAI API key
client = OpenAI(api_key=OPENAI_API_KEY)

# Load CLIP model for local image-text embedding
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def to_numpy(tensor: torch.Tensor) -> np.ndarray:
    """
    Convert PyTorch tensor to NumPy array.

    Args:
        tensor (torch.Tensor): Input tensor.

    Returns:
        np.ndarray: Float32 NumPy array.
    """
    return tensor.detach().cpu().numpy().astype(np.float32)


# -----------------------------
# --- Embedding Functions ---
# -----------------------------

def embed_text(text: str) -> np.ndarray:
    """
    Generate an embedding for input text using OpenAI's embedding API.

    Args:
        text (str): Text input.

    Returns:
        np.ndarray: 768-dimensional embedding vector (or zero-vector fallback).
    """
    try:
        response = client.embeddings.create(
            input=[text],
            model="text-embedding-ada-002"
        )
        return np.array(response.data[0].embedding, dtype=np.float32)
    except Exception as e:
        print(f"⚠️ embed_text failed: {e}")
        return np.zeros(1536, dtype=np.float32)

def embed_query_for_image_search(text: str) -> np.ndarray:
    """
    Generate a CLIP text embedding for semantic image search.

    Args:
        text (str): Search query.

    Returns:
        np.ndarray: 512-dimensional CLIP text embedding.
    """
    inputs = clip_processor(text=[text], return_tensors="pt", padding=True)
    with torch.no_grad():
        text_features = clip_model.get_text_features(**inputs)
    return to_numpy(text_features[0])


def embed_image(image_bytes: bytes) -> np.ndarray:
    """
    Generate a CLIP image embedding for visual similarity tasks.

    Args:
        image_bytes (bytes): Image data in bytes format.

    Returns:
        np.ndarray: 512-dimensional CLIP image embedding.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = clip_processor(images=image, return_tensors="pt")
    with torch.no_grad():
        image_features = clip_model.get_image_features(**inputs)
    return to_numpy(image_features[0])