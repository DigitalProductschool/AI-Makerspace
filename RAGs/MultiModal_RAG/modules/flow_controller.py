"""
Flow controller module orchestrating the multimodal RAG pipeline using LangGraph.
Responsible for query classification, retrieval, decision-making, response generation,
image inclusion logic, and final formatting with guardrails validation.
"""

from langgraph.graph import StateGraph, END
from guardrails import Guard
from modules import retriever, llm_respond, memory
from modules.utils import safe_log, deduplicate_images_by_caption
from typing import Dict, TypedDict, Optional
import time

# --- Define ChatState Schema for LangGraph ---

class ChatState(TypedDict, total=False):
    user_id: str
    doc_id: str
    query: str
    context: str
    image: Optional[dict]
    rag_caption: Optional[str]
    raw_response: dict
    final_response: dict
    next: str

# --- Load Guardrails for Output Validation ---
guard = Guard.from_rail("rails/response_validator.rail")


# --- ROUTER Function ---
def decision_router(state: Dict) -> str:
    """Routing function based on state['next'] field."""
    return state["next"]


# --- STEP 1: Classify Query ---
def is_general_query_step(state: Dict) -> Dict:
    """
    Determines if a query is general (overview-type) or specific (targeted).
    Routes to appropriate retrieval strategy.
    """
    query = state["query"].strip().lower()
    general_keywords = [
        "purpose", "overview", "summary", "introduction",
        "what is this", "about this manual"
    ]
    is_general = any(k in query for k in general_keywords)

    return {**state, "next": "retrieve_general" if is_general else "retrieve_specific"}


# --- STEP 2A: General Text Retrieval ---
def retrieve_general_step(state: Dict) -> Dict:
    """Retrieves the full document and session context for general queries."""
    doc_id = state["doc_id"]
    user_id = state["user_id"]

    memory_context = memory.load_session_context(user_id=user_id, doc_id=doc_id)
    all_text = retriever.get_all_chunks(doc_id)

    return {
        **state,
        "context": memory_context + "\n" + all_text,
        "image": None,
        "rag_caption": None,
    }


# --- STEP 2B: Specific Text + Image Retrieval ---
def retrieve_specific_step(state: Dict) -> Dict:
    """Retrieves specific text chunks, relevant images, and captions for the query."""
    doc_id = state["doc_id"]
    query = state["query"]
    user_id = state["user_id"]

    memory_context = memory.load_session_context(user_id=user_id, doc_id=doc_id)
    relevant_text, relevant_images, rag_captions = retriever.get_relevant_content(doc_id, query)

    return {
        **state,
        "context": memory_context + "\n" + relevant_text,
        "image": relevant_images,
        "rag_caption": rag_captions,
    }


# --- STEP 3: Image Inclusion Decision ---
def decision_step(state: Dict) -> Dict:
    """Decides whether an image should be included in the response based on relevance."""
    safe_log("🧭 Deciding whether to include image...")

    query = state["query"]
    images = state.get("image", []) or []
    captions = state.get("rag_caption", []) or []

    safe_log(f"[DEBUG] Query passed to decision: {query}")
    safe_log(f"[DEBUG] Captions passed to decision: {captions}")

    selected_images = []
    selected_captions = []

    for img, cap in zip(images, captions):
        if not cap:
            continue
        if llm_respond.should_include_image(query, cap):
            selected_images.append(img)
            selected_captions.append(cap)

    if selected_images:
        # Limit to 1 image for clarity and deduplicate
        selected_images, selected_captions = deduplicate_images_by_caption(
            selected_images, selected_captions
        )
        selected_images = selected_images[:1]
        selected_captions = selected_captions[:1]

        state["image"] = selected_images
        state["rag_caption"] = selected_captions
        next_step = "generate_with_image"
    else:
        state["image"] = []
        state["rag_caption"] = []
        next_step = "generate_without_image"

    return {**state, "next": next_step}


# --- STEP 4: LLM Generation ---
def generate_step(state: Dict, with_image: bool) -> Dict:
    """Calls LLM with or without image input to generate the assistant response."""
    images = state.get("image", []) if with_image else []

    result = llm_respond.generate_response(
        query=state["query"],
        context=state["context"],
        images=images
    )

    return {**state, "raw_response": result}


def generate_with_image(state: Dict) -> Dict:
    return generate_step(state, with_image=True)


def generate_without_image(state: Dict) -> Dict:
    return generate_step(state, with_image=False)


# --- STEP 5: Output Validation ---
def validate_step(state: Dict) -> Dict:
    """Validates and finalizes the raw LLM response using Guardrails."""
    response = state.get("raw_response", {})

    final = {
        "text": response.get("text", ""),
        "images": response.get("images", []),
        "image_captions": response.get("image_captions", []),
        "image_explanation": state.get("rag_caption", ""),
    }

    return {**state, "final_response": final}


# --- BUILD LangGraph ---
builder = StateGraph(state_schema=ChatState)

# Register flow nodes
builder.set_entry_point("classify_query")
builder.add_node("classify_query", is_general_query_step)
builder.add_node("retrieve_general", retrieve_general_step)
builder.add_node("retrieve_specific", retrieve_specific_step)
builder.add_node("decide", decision_step)
builder.add_node("generate_with_image", generate_with_image)
builder.add_node("generate_without_image", generate_without_image)
builder.add_node("validate", validate_step)

# Define graph transitions
builder.add_conditional_edges("classify_query", decision_router, {
    "retrieve_general": "retrieve_general",
    "retrieve_specific": "retrieve_specific"
})
builder.add_edge("retrieve_general", "decide")
builder.add_edge("retrieve_specific", "decide")
builder.add_conditional_edges("decide", decision_router, {
    "generate_with_image": "generate_with_image",
    "generate_without_image": "generate_without_image"
})
builder.add_edge("generate_with_image", "validate")
builder.add_edge("generate_without_image", "validate")
builder.add_edge("validate", END)

# Compile graph
graph = builder.compile()

# Optional visualization (comment if deploying)
print(graph.get_graph().draw_mermaid())


# --- Unified Flow Runner ---
def run_flow(user_id: str, doc_id: str, query: str) -> Dict:
    """
    Entrypoint to execute the full retrieval-generation-validation pipeline.

    Args:
        user_id (str): User identifier.
        doc_id (str): Uploaded document identifier.
        query (str): Natural language user query.

    Returns:
        dict: Final validated response with optional images.
    """
    state = {
        "user_id": user_id,
        "doc_id": doc_id,
        "query": query
    }

    final_state = graph.invoke(state)
    response = final_state.get("final_response", {})

    # Save interaction to memory unless it's a warning
    if response.get("text") and not response["text"].startswith("⚠️"):
        memory.save_turn(user_id, doc_id, query, response["text"])
        time.sleep(1)  # simulate async saving

    return response