"""
PDF parser module for extracting structured text and images from manuals.
- Uses LlamaParse for text extraction.
- Uses PyMuPDF for image extraction.
- Auto-captions images using GPT-based vision model.
"""

import os
import uuid
import fitz
import tempfile
from llama_parse import LlamaParse
from tenacity import retry, wait_exponential, stop_after_attempt

from modules.config import LLAMAPARSE_API_KEY
from modules.utils import clean_text, safe_log
from modules.llm_respond import caption_image_with_vision_llm

@retry(wait=wait_exponential(min=2, max=30), stop=stop_after_attempt(5))
def safe_load_data(parser, file_path):
    """Retry wrapper for LlamaParse document loading."""
    return parser.load_data(file_path)

def process_pdf(uploaded_pdf, save_images=True, save_dir="data/images"):
    """
    Parses the uploaded PDF:
    - Extracts clean text chunks with page metadata.
    - Extracts embedded images and generates captions using context from the page.
    
    Args:
        uploaded_pdf: Streamed PDF file from Streamlit uploader.
        save_images (bool): Whether to save extracted images to disk.
        save_dir (str): Directory path to store images.

    Returns:
        dict: {
            "doc_id": str,
            "text_chunks": List[Dict],
            "images": List[Dict]
        }
    """
    doc_id = str(uuid.uuid4())
    temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

    # Save uploaded file temporarily
    with open(temp_path, "wb") as f:
        f.write(uploaded_pdf.read())
    safe_log(f"📄 Temp PDF saved at {temp_path}")

    # Initialize parser
    parser = LlamaParse(api_key=LLAMAPARSE_API_KEY, result_type="markdown")

    # Step 1: Extract text
    try:
        documents = safe_load_data(parser, temp_path)
    except Exception as e:
        safe_log(f"⚠️ Text extraction failed: {e}")
        documents = []

    text_chunks = [
        {
            "text": clean_text(doc.text),
            "page": idx + 1,
            "source": f"page_{idx + 1}"
        }
        for idx, doc in enumerate(documents)
    ]
    safe_log(f"✅ Parsed {len(text_chunks)} text chunks.")

    # Step 2: Extract images and captions
    image_list = []
    pdf_doc = fitz.open(temp_path)

    if save_images:
        os.makedirs(save_dir, exist_ok=True)
        safe_log(f"📂 Image save dir ensured: {save_dir}")

    for page_index in range(len(pdf_doc)):
        page = pdf_doc[page_index]
        page_text = page.get_text("text")

        # Attempt to extract page title/header
        header_text = ""
        blocks = page.get_text("blocks")
        if blocks:
            header_candidates = sorted(blocks, key=lambda b: b[1])  # top-most block
            header_text = header_candidates[0][4].strip() if header_candidates else ""

        context = f"{header_text}\n\n{page_text}".strip()

        for img_index, img in enumerate(page.get_images(full=True)):
            try:
                xref = img[0]
                base_image = pdf_doc.extract_image(xref)
                image_bytes = base_image["image"]
                ext = base_image["ext"]

                caption = caption_image_with_vision_llm(image_bytes, context)

                # Save image to disk if enabled
                if save_images:
                    filename = f"{doc_id}_page{page_index + 1}_img{img_index + 1}.{ext}"
                    image_path = os.path.join(save_dir, filename)
                    with open(image_path, "wb") as out:
                        out.write(image_bytes)
                    safe_log(f"💾 Image saved to {image_path}")

                image_list.append({
                    "image_bytes": image_bytes,
                    "caption": caption,
                    "page": page_index + 1,
                    "source": f"page_{page_index + 1}",
                    "ext": ext
                })

            except Exception as e:
                safe_log(f"⚠️ Failed image on page {page_index + 1}: {e}")

    safe_log(f"✅ Extracted {len(image_list)} images.")

    return {
        "doc_id": doc_id,
        "text_chunks": text_chunks,
        "images": image_list
    }