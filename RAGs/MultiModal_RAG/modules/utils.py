"""
Utility functions for text processing, image handling, PDF mocking, and similarity scoring.
"""

import os
import io
import re
import base64
import textwrap
import hashlib
import random
import numpy as np
from io import BytesIO
from typing import List, Tuple, Optional
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from modules.embedding_utils import embed_text


# -----------------------
# --- Text Utilities ---
# -----------------------

def clean_text(text: str) -> str:
    """Normalize whitespace and newlines in a string."""
    return re.sub(r'\s+', ' ', text.strip())


def chunk_text(text: str, max_tokens: int = 512) -> List[str]:
    """
    Split text into smaller chunks based on sentence boundaries.

    Args:
        text (str): Raw text input.
        max_tokens (int): Approximate token limit per chunk.

    Returns:
        List[str]: List of split and grouped text chunks.
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_tokens:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


def extract_caption_text(caption: str, max_length: int = 200) -> str:
    """Truncate captions to a safe length for prompt injection."""
    return textwrap.shorten(caption.strip(), width=max_length, placeholder="...")


def safe_log(msg: str) -> None:
    """Simple console logger."""
    print(f"[LOG] {msg}")


# -------------------------
# --- Image Conversion ---
# -------------------------

def encode_image_to_base64(img: Image.Image, format: str = "JPEG") -> str:
    """Convert PIL image to base64-encoded string."""
    buffer = io.BytesIO()
    img.save(buffer, format=format)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def decode_base64_to_image(b64_string: str) -> Image.Image:
    """Convert base64-encoded string back to PIL image."""
    img_bytes = base64.b64decode(b64_string)
    return Image.open(io.BytesIO(img_bytes))


def resize_image(img: Image.Image, max_dim: int = 512) -> Image.Image:
    """Resize image while preserving aspect ratio."""
    img.thumbnail((max_dim, max_dim))
    return img


# -------------------------------
# --- PDF and Diagram Mockers ---
# -------------------------------

def create_dummy_image_bytes() -> bytes:
    """Create a synthetic image representing an autofocus diagram."""
    img = Image.new("RGB", (400, 300), color="white")
    draw = ImageDraw.Draw(img)

    draw.rectangle([40, 100, 100, 160], fill="gray", outline="black")
    draw.rectangle([300, 100, 360, 160], fill="lightblue", outline="black")
    draw.line([100, 130, 300, 130], fill="red", width=4)

    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    draw.text((50, 165), "Lens", fill="black", font=font)
    draw.text((310, 165), "Sensor", fill="black", font=font)
    draw.text((180, 110), "Focus", fill="black", font=font)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()


def create_test_pdf(text: str) -> BytesIO:
    """Create a single-page mock PDF with embedded autofocus diagram."""
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # Draw sample instructional text
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, text)

    # Embed a dummy image diagram
    img = Image.new("RGB", (320, 240), color="white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 90, 80, 150], fill="lightgray", outline="black")
    draw.rectangle([240, 90, 300, 150], fill="lightblue", outline="black")
    draw.line([80, 120, 240, 120], fill="red", width=3)
    draw.text((30, 155), "Lens", fill="black")
    draw.text((245, 155), "Sensor", fill="black")
    draw.text((140, 100), "Focus", fill="black")

    img_path = "temp_camera_diagram.jpg"
    img.save(img_path)
    c.drawImage(img_path, 100, 500, width=320, height=240)
    os.remove(img_path)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer


def create_camera_manual_mock_pdf() -> BytesIO:
    """Generate a multi-page mock camera manual with embedded diagrams."""
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)

    pages = [
        ("Manual Purpose", "This manual explains basic usage of the Canon EOS Rebel T3 / 1100D."),
        ("Autofocus Feature", "Set the lens to AF and press the shutter halfway. [Image Caption: Autofocus Switch]"),
        ("Manual Focus", "Switch to MF and rotate the focusing ring. [Image Caption: Manual Focus Control]"),
        ("Live View AF Modes", 
         "Live Mode: Contrast detection. [Image Caption: Live Mode UI]\n"
         "Face Detection: Tracks faces. [Image Caption: Face Detection UI]\n"
         "Quick Mode: Uses phase detection. [Image Caption: Quick Mode UI]"),
        ("Sports Mode", "Use Sports (5) for 3fps. [Image Caption: Sports Mode Dial] [Image Caption: Panning Example]"),
        ("Battery and Card", "Insert battery and SD card. [Image Caption: Battery Step] [Image Caption: SD Card Step]"),
        ("LCD Issues", "Screen may lag in extreme temperatures."),
        ("Movie Mode", "Shoot HD at 1280x720. [Image Caption: Movie Mode UI]"),
        ("Cold Weather Tips", "Keep batteries warm. [Image Caption: Cold Weather Warning]"),
        ("(Empty)", "")
    ]

    img_counter = 0
    for title, text in pages:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 750, title)

        c.setFont("Helvetica", 12)
        for idx, line in enumerate(textwrap.wrap(text, width=80)):
            c.drawString(50, 730 - 15 * idx, line)

        captions = (
            ["Live Mode UI", "Face Detection UI", "Quick Mode UI"]
            if title == "Live View AF Modes"
            else re.findall(r"\[Image Caption: (.*?)\]", text)
        )

        for caption in captions:
            img = Image.new("RGB", (320, 240), color="white")
            draw = ImageDraw.Draw(img)
            draw.rectangle([20, 90, 80, 150], fill="lightgray", outline="black")
            draw.rectangle([240, 90, 300, 150], fill="lightblue", outline="black")
            draw.line([80, 120, 240, 120], fill="red", width=3)

            try:
                font = ImageFont.truetype("arial.ttf", 32)
            except:
                font = ImageFont.load_default()

            bbox = font.getbbox(caption)
            text_x = (320 - (bbox[2] - bbox[0])) / 2
            text_y = (240 - (bbox[3] - bbox[1])) / 2
            draw.text((text_x, text_y), caption, fill="black", font=font)

            img_path = f"temp_camera_diagram_{img_counter}.jpg"
            img.save(img_path)
            c.drawImage(img_path, 100, 500 - 220 * img_counter, width=200, height=150)
            os.remove(img_path)

            img_counter += 1

        c.showPage()

    c.save()
    buffer.seek(0)
    return buffer


# ---------------------------
# --- Similarity + Rerank ---
# ---------------------------

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8)


def select_relevant_images(images: List[dict], query: str, top_k: int = 1) -> List[dict]:
    """Return top-k most relevant images based on caption-query embedding similarity."""
    if not images:
        return []

    query_emb = embed_text(query)
    scored = []

    for img in images:
        caption = img.get("caption", "")
        if not caption:
            continue
        caption_emb = embed_text(caption)
        sim = cosine_similarity(query_emb, caption_emb)
        scored.append((sim, img))

    scored.sort(reverse=True)
    return [img for _, img in scored[:top_k]]


def deduplicate_images_by_caption(images: List[dict], captions: List[str]) -> Tuple[List[dict], List[str]]:
    """
    Remove images with duplicate captions (based on MD5 hash of caption).

    Returns:
        Tuple of (unique_images, unique_captions)
    """
    seen = set()
    unique_images, unique_captions = [], []

    for img, cap in zip(images, captions):
        cap_key = hashlib.md5(cap.strip().lower().encode()).hexdigest()
        if cap_key not in seen:
            seen.add(cap_key)
            unique_images.append(img)
            unique_captions.append(cap)

    return unique_images, unique_captions