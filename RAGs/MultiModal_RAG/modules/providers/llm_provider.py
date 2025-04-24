"""
LLM Provider Module
Handles interaction with OpenAI and TogetherAI LLM APIs, including vision-enabled chat.
"""

import os
import requests
import base64
import time
import logging
from llama_index.llms.openai import OpenAI
from modules.config import OPENAI_API_KEY, TOGETHER_API_KEY, ACTIVE_PROVIDER, TOGETHER_CHAT_COMPLETIONS_URL

# --- Initialize OpenAI LLM (default) ---
openai_llm = OpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY,
    temperature=0.3,
    max_tokens=1000,
)

def chat_with_openai(messages):
    """
    Chat using the default OpenAI model (gpt-4o).

    Args:
        messages (List[dict]): Messages in ChatML format.

    Returns:
        str: LLM response.
    """
    return openai_llm.chat(messages=messages)

def chat_with_gpt4o(messages):
    """
    Dedicated minimal-chat wrapper for GPT-4o with low temperature.

    Args:
        messages (List[dict]): Chat prompt blocks.

    Returns:
        str: Response content.
    """
    temp_llm = OpenAI(
        model="gpt-4o",
        api_key=OPENAI_API_KEY,
        temperature=0.0,
        max_tokens=100,
    )
    return temp_llm.chat(messages=messages)

# --- Helper: Serialize Messages for TogetherAI ---
def serialize_message_blocks_for_together(messages):
    """
    Converts message blocks to TogetherAI-compatible schema.

    Args:
        messages (List[dict|ChatMessage]): LLM chat messages.

    Returns:
        List[dict]: Serialized messages.
    """
    serialized = []

    for msg in messages:
        if isinstance(msg, dict):
            serialized.append({
                "role": msg.get("role", "user"),
                "content": msg.get("content", "")
            })
            continue

        role = getattr(msg, "role", "user")
        role = role.value if hasattr(role, "value") else role
        content = getattr(msg, "content", msg.__dict__.get("content", ""))

        if isinstance(content, (str, list)):
            serialized.append({"role": role, "content": content})
        else:
            raise ValueError(f"Unsupported content format: {type(content)}")

    return serialized

# --- Chat with TogetherAI (Vision-Supportive) ---
def chat_with_together(messages):
    """
    Sends a chat request to TogetherAI with support for multimodal content.

    Args:
        messages (List[dict]): Message blocks (text + image).

    Returns:
        str: Combined response.
    """
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    full_serialized = serialize_message_blocks_for_together(messages)
    content_block = full_serialized[0]["content"]

    images, text_parts = [], []

    # Detect structure of message
    if isinstance(content_block, list):
        for part in content_block:
            if part.get("type") == "image":
                images.append(part["image"])
            elif part.get("type") == "text":
                text_parts.append(part["text"])
    elif isinstance(content_block, str):
        text_parts.append(content_block)
    else:
        raise ValueError("Unexpected content format for TogetherAI message.")

    # If <=1 image, send normally
    if len(images) <= 1:
        payload = {
            "model": "meta-llama/Llama-Vision-Free",
            "messages": full_serialized,
            "max_tokens": 1000,
        }
        return _post_together(payload, headers)

    # If multiple images, split and combine responses
    combined_response = ""
    for idx, img in enumerate(images):
        mini_message = [{
            "role": "user",
            "content": [{"type": "text", "text": "\n".join(text_parts)}, {"type": "image", "image": img}]
        }]
        payload = {
            "model": "meta-llama/Llama-Vision-Free",
            "messages": mini_message,
            "max_tokens": 1000,
        }
        partial = _post_together(payload, headers)
        combined_response += f"\n\n--- Image Part {idx + 1} ---\n{partial.strip()}"

    return combined_response.strip()

# --- Retry Wrapper for POST ---
def _post_together(payload, headers):
    """
    Robust POST request to TogetherAI with retry support.

    Args:
        payload (dict): JSON body.
        headers (dict): Auth and content headers.

    Returns:
        str: Chat response content.
    """
    max_retries = 5
    for attempt in range(max_retries):
        try:
            logging.info(f"[TOGETHER] Attempt {attempt + 1}")
            response = requests.post(TOGETHER_CHAT_COMPLETIONS_URL, headers=headers, json=payload)

            if response.status_code == 429:
                wait_time = 2 ** attempt
                logging.warning(f"[TOGETHER] Rate limit hit. Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue

            if response.status_code != 200:
                logging.error(f"[TOGETHER] Response Error: {response.status_code} — {response.text}")
                response.raise_for_status()

            return response.json()["choices"][0]["message"]["content"]

        except requests.RequestException as e:
            logging.exception(f"[TOGETHER] Request failed on attempt {attempt + 1}: {e}")
            if attempt == max_retries - 1:
                raise RuntimeError("🚨 Failed after max retries.") from e

    raise RuntimeError("🚨 Max retries exceeded with rate limit errors.")

# --- Provider-Agnostic Chat Entry Point ---
def unified_chat(messages):
    """
    Calls chat function from the selected provider.

    Args:
        messages (List): Chat message blocks.

    Returns:
        str: Chat response.
    """
    provider = ACTIVE_PROVIDER.lower()
    if provider == "openai":
        return chat_with_openai(messages)
    elif provider == "together":
        return chat_with_together(messages)
    else:
        raise ValueError(f"Unsupported ACTIVE_PROVIDER: {ACTIVE_PROVIDER}")