"""
LLM response generation and image captioning utilities.
Uses multimodal prompts to produce responses and image captions for PDF content.
"""

import base64
import json
import re
from typing import List, Dict, Optional
import guardrails as gd
from llama_index.core.llms import ChatMessage, TextBlock, ImageBlock, MessageRole
from modules.providers.llm_provider import unified_chat, chat_with_gpt4o
from modules.utils import extract_caption_text, safe_log

# --- Load Guardrails for response validation ---
guard = gd.Guard.from_rail("rails/response_validator.rail")


def clean_json_string(json_str: str) -> str:
    """
    Cleans JSON string by removing markdown code fences and trimming whitespace.

    Args:
        json_str (str): Raw JSON string.

    Returns:
        str: Cleaned JSON string.
    """
    cleaned = re.sub(r"^```(?:json)?\s*", "", json_str.strip(), flags=re.IGNORECASE)
    return re.sub(r"\s*```$", "", cleaned).strip()


def generate_response(query: str, context: str, images: Optional[List[Dict]] = None) -> Dict:
    """
    Generates a structured response using a multimodal LLM with optional image input.

    Args:
        query (str): User query.
        context (str): Textual context from PDF.
        images (List[Dict], optional): List of image dictionaries with base64 and caption.

    Returns:
        Dict: Dictionary with validated response text, images, and image captions.
    """
    blocks = [
        TextBlock(
            text=(
                "You are a helpful assistant answering questions using the following context, which was retrieved from a PDF manual uploaded by the user.\n"
                "Use this structure:\n"
                "1. **Summary** – Answer concisely based on the document.\n"
                "2. **Image** – Include if an image is provided.\n"
                "3. **Image Explanation** – Use image caption if available.\n\n"
                "Rules:\n"
                "- Respond in English.\n"
                "- Do not hallucinate.\n"
                "- Return your answer in this JSON format:\n\n"
                '{ "text": "<your answer>" }'
                f"\n\nContext:\n{context}\n\nUser Question: {query}"
            )
        )
    ]

    # Add image blocks if provided
    if images:
        for img in images:
            try:
                image_bytes = base64.b64decode(img["image_b64"])
                blocks.append(ImageBlock(image=image_bytes, image_mimetype="image/jpeg"))

                caption = extract_caption_text(img.get("caption", ""))
                if caption:
                    blocks.append(TextBlock(text=f"Image Caption: {caption}"))
                    safe_log(f"🖼️ Image added with caption: {caption}")
            except Exception as e:
                safe_log(f"⚠️ Failed to decode image: {e}")

    # Send to LLM
    response = unified_chat(messages=[ChatMessage(role=MessageRole.USER, blocks=blocks)])
    raw_json_str = response.strip() if isinstance(response, str) else response.message.content.strip()

    # Clean and validate
    cleaned_str = clean_json_string(raw_json_str)
    safe_log(f"[LLM] Cleaned response: {cleaned_str}")

    try:
        parsed = guard.parse(llm_output=cleaned_str)
        validated = parsed.validated_output or cleaned_str
        validated_dict = validated if isinstance(validated, dict) else json.loads(validated)
        safe_log("[GUARDRAILS] ✅ Output validated.")
    except Exception as e:
        safe_log(f"[GUARDRAILS] ❌ Validation failed: {e}")
        try:
            validated_dict = json.loads(cleaned_str)
            safe_log("[FALLBACK] JSON parsed without guard.")
        except Exception as fallback_e:
            safe_log(f"[FALLBACK] Fallback parsing failed: {fallback_e}")
            validated_dict = {"text": cleaned_str}

    final_response = {
        "text": validated_dict.get("text", "").strip(),
        "images": images or [],
        "image_captions": [img.get("caption") for img in images if img.get("caption")] if images else []
    }

    safe_log("[FINAL RESPONSE]")
    safe_log(f"📝 Text Preview: {final_response['text'][:200]}...")
    safe_log(f"🖼️ Total Images: {len(final_response['images'])}")
    return final_response


def caption_image_with_vision_llm(image_bytes: bytes, context: Optional[str] = None) -> str:
    """
    Generates a short factual caption for a given image using LLM.

    Args:
        image_bytes (bytes): Image data in bytes.
        context (str, optional): Additional text context to aid captioning.

    Returns:
        str: Caption text.
    """
    safe_log("[STEP] 🖼️ Generating standalone image caption...")
    try:
        prompt = (
            "You are a technical documentation expert.\n"
            "Describe the image in short, factual terms only.\n"
            "Avoid assumptions or opinions. Output plain text only."
        )
        if context:
            prompt += f"\n\nContext:\n{context[:500]}"

        response = unified_chat(messages=[
            ChatMessage(role=MessageRole.USER, blocks=[
                TextBlock(text=prompt),
                ImageBlock(image=image_bytes, image_mimetype="image/jpeg")
            ])
        ])

        caption = response.strip() if isinstance(response, str) else response.message.content.strip()
        safe_log("[VISION] ✅ Caption generated.")
        return caption

    except Exception as e:
        safe_log(f"⚠️ Image captioning failed: {e}")
        return ""


def generate_rag_caption(image_bytes: bytes, query: str, context: Optional[str] = None) -> str:
    """
    Generates a context-aware image caption based on a user query.

    Args:
        image_bytes (bytes): Image data in bytes.
        query (str): User question.
        context (str, optional): Textual context from the document.

    Returns:
        str: Generated caption.
    """
    safe_log("[STEP] 🖼️ Generating RAG-style caption...")
    try:
        prompt = (
            f"What is shown in this image in relation to the user question: '{query}'?\n"
            "Focus on what is visually present only."
        )
        if context:
            prompt += f"\n\nHelpful document context:\n{context[:500]}"

        response = unified_chat(messages=[
            ChatMessage(role=MessageRole.USER, blocks=[
                TextBlock(text=prompt),
                ImageBlock(image=image_bytes, image_mimetype="image/jpeg")
            ])
        ])

        caption = response.strip() if isinstance(response, str) else response.message.content.strip()
        safe_log("[VISION] ✅ RAG caption generated.")
        return caption

    except Exception as e:
        safe_log(f"⚠️ RAG captioning failed: {e}")
        return ""


def decide_if_image_should_be_used(query: str, caption: str) -> bool:
    """
    Decides if an image should be shown to the user based on the query and its caption.

    Args:
        query (str): User query.
        caption (str): Image caption.

    Returns:
        bool: True if image should be shown, False otherwise.
    """
    safe_log("[STEP] 🧭 Deciding image relevance...")
    prompt = (
            "Given the user question and the caption of a related image, decide whether the image should be shown.\n"
            "Respond ONLY with 'yes' or 'no'.\n"
            "NO extra text, NO explanations.\n"
            f"Question: {query}\n"
            f"Image Caption: {caption}"
        )

    try:
        response = chat_with_gpt4o(messages=[
            ChatMessage(role=MessageRole.USER, blocks=[TextBlock(text=prompt)])
        ])
        decision = response.strip().lower() if isinstance(response, str) else response.message.content.strip().lower()
        safe_log(f"[DECISION] Result: {decision}")
        return decision == "yes"
    except Exception as e:
        safe_log(f"⚠️ Decision logic failed: {e}")
        return False


# Alias for compatibility
def should_include_image(query: str, image_caption: str) -> bool:
    """
    Alias for decide_if_image_should_be_used().
    """
    return decide_if_image_should_be_used(query, image_caption)