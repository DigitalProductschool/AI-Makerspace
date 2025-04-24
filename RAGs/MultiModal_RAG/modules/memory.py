"""
Memory module for session persistence using Mem0.
Stores and retrieves conversational context based on user and document IDs.
"""

from typing import Union
from mem0 import MemoryClient
from modules.config import MEM0_API_KEY
from modules.utils import safe_log

# --- Initialize Mem0 Client ---
client = MemoryClient(api_key=MEM0_API_KEY)

def load_session_context(user_id: str, doc_id: str, k: int = 5) -> str:
    """
    Retrieves the last k memory messages for a given user and document.

    Args:
        user_id (str): Identifier for the user.
        doc_id (str): Identifier for the document.
        k (int): Number of messages to retrieve (default: 5).

    Returns:
        str: A concatenated string of recent memory messages.
    """
    filters = {
        "AND": [
            {"user_id": user_id},
            {"doc_id": doc_id}  # ✅ Use flat key here
        ]
    }

    try:
        raw = client.get_all(filters=filters, version="v2", output_format="v1.1")
        results = raw.get("results", [])
        safe_log(f"[MEMORY] Retrieved {len(results)} memory blocks for user={user_id}, doc={doc_id}")
    except Exception as e:
        safe_log(f"[ERROR] Failed to fetch memories: {e}")
        return ""

    all_messages = []
    for mem in results:
        msgs = mem.get("messages", [])
        if msgs:
            safe_log(f"[DEBUG] Messages from memory block: {msgs}")
            all_messages.extend(msgs)
        elif "memory" in mem:
            fallback = mem["memory"]
            safe_log(f"[DEBUG] Using fallback memory field: {fallback}")
            all_messages.append({"content": fallback})

    recent = all_messages[-k:]
    context = "\n".join([msg.get("content", "") for msg in recent if msg.get("content")])
    safe_log(f"[MEMORY] Loaded context:\n{context}")
    return context


def save_turn(user_id: str, doc_id: str, query: str, response: Union[str, dict]) -> None:
    """
    Saves a turn (user query and LLM response) into memory.

    Args:
        user_id (str): Identifier for the user.
        doc_id (str): Identifier for the document.
        query (str): User's question.
        response (Union[str, dict]): Assistant's reply (text or dict with "text").
    """
    response_text = response.get("text") if isinstance(response, dict) else str(response)
    if not response_text:
        safe_log(f"[WARNING] No valid text to save for user={user_id}")
        return

    safe_log(f"[MEMORY] Saving turn for user={user_id}, doc={doc_id}:\nUser: {query}\nAssistant: {response_text}")

    try:
        client.add(
            messages=[
                {"role": "user", "content": query},
                {"role": "assistant", "content": response_text}
            ],
            user_id=user_id,
            metadata={"doc_id": doc_id},
            sync=True
        )
        safe_log("[MEMORY] ✅ Turn saved successfully.")
    except Exception as e:
        safe_log(f"[ERROR] Failed to save memory turn: {e}")