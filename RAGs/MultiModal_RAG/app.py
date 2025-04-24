"""
Streamlit frontend for MANUAMIND: a multimodal RAG chatbot.
Features:
- PDF parsing with image captioning
- Conversational UI
- Memory + audio response
"""

import streamlit as st
import logging
import pickle
import os
from modules import pdf_parser, memory, retriever, llm_respond, flow_controller, tts
from modules.utils import decode_base64_to_image, safe_log

# --- App Config ---
logging.basicConfig(level=logging.INFO)
st.set_page_config(page_title="MANUAMIND", layout="wide")
st.title("📘 MANUAMIND — Instruction-Bound Multimodal Chatbot")

DEV_MODE = True
PICKLE_PATH = "data/parsed_doc.pkl"

# --- Initialize Session State ---
st.session_state.setdefault("chat_history", [])
st.session_state.setdefault("doc_id", None)
st.session_state.setdefault("pending_response", False)
st.session_state.setdefault("doc_ready", False)
st.session_state.setdefault("indexed", False)

# --- Load Cached PDF in Dev Mode ---
if DEV_MODE and os.path.exists(PICKLE_PATH) and not st.session_state.doc_ready:
    with st.spinner("🔄 Loading cached document..."):
        safe_log("DEV: Loading from pickle")
        with open(PICKLE_PATH, "rb") as f:
            parsed = pickle.load(f)

        st.session_state.doc_id = parsed["doc_id"]
        st.session_state.chunks = parsed["text_chunks"]
        st.session_state.images = parsed["images"]
        st.session_state.doc_ready = True

        if "qdrant_client" not in st.session_state:
            retriever.get_qdrant()

        safe_log(f"✅ Cached document loaded: {parsed['doc_id']}")
        st.markdown(f"🧪 **DEV MODE ACTIVE** — Document: `{parsed['doc_id']}`")

# --- Sidebar: Upload & Index PDF ---
with st.sidebar:
    st.header("📄 Upload Manual")
    uploaded_pdf = st.file_uploader("Upload a PDF manual", type="pdf")

    if uploaded_pdf and not st.session_state.doc_ready:
        with st.spinner("📚 Parsing uploaded document..."):
            parsed = pdf_parser.process_pdf(uploaded_pdf)
            st.session_state.doc_id = parsed["doc_id"]
            st.session_state.chunks = parsed["text_chunks"]
            st.session_state.images = parsed["images"]
            st.session_state.doc_ready = True

            if not st.session_state.indexed:
                retriever.index_chunks(parsed["doc_id"], parsed["text_chunks"])
                retriever.index_images(parsed["doc_id"], parsed["images"])
                st.session_state.indexed = True
                safe_log("✅ Indexed text and images.")

            os.makedirs("data", exist_ok=True)
            with open(PICKLE_PATH, "wb") as f:
                pickle.dump(parsed, f)

            st.success("✅ Document processed and cached.")

    if st.session_state.doc_ready:
        st.markdown(f"**Loaded Document ID:** `{st.session_state.doc_id}`")

    st.divider()
    st.toggle("🔊 Audio Response", key="audio_enabled", value=True)

# --- Image Renderer ---
def render_image_section(image_data: dict, caption: str = ""):
    """Render base64-encoded image with caption."""
    try:
        image = decode_base64_to_image(image_data["image_b64"])
        w, h = image.size
        display_width = int(min(1.0, max(0.4, 500 / w)) * w)

        st.image(image, width=display_width)
        if caption:
            st.markdown(f"🖼️ **Caption:** {caption}")
        st.markdown("---")
    except Exception as e:
        st.warning("⚠️ Could not render image.")
        logging.warning(f"[RENDER] Failed: {e}")

# --- Main Chat Window ---
st.markdown("### 💬 Conversation")
scroll_anchor = st.empty()

for turn in st.session_state.chat_history:
    with st.container():
        st.markdown(f"🧑 **You:** {turn['q']}")
        st.markdown("🤖 **Bot Response:**")
        st.markdown(turn['a'])

        # Optional TTS playback
        if st.session_state.audio_enabled and turn.get("a"):
            try:
                audio_bytes = tts.text_to_audio(turn["a"])
                st.audio(audio_bytes, format="audio/mp3")
            except Exception as e:
                st.warning("⚠️ Audio failed.")
                logging.warning(f"[TTS] Failed: {e}")

        # Optional image rendering
        for img_meta in turn.get("images", []):
            if img_meta.get("image", {}).get("image_b64"):
                render_image_section(img_meta["image"], img_meta.get("caption", ""))

        st.markdown("---")

scroll_anchor.markdown("<div id='end'></div>", unsafe_allow_html=True)

# --- Bot Thinking Placeholder ---
if st.session_state.pending_response and st.session_state.get("pending_user_query"):
    with st.container():
        st.markdown(f"🧑 **You:** {st.session_state.pending_user_query}")
        with st.spinner("🧠 Thinking..."):
            st.markdown("🤖 **Bot is generating a response...**")
        st.markdown("---")

# --- Smooth Scroll to Bottom ---
st.markdown("""
<script>
    var el = document.getElementById("end");
    if (el) el.scrollIntoView({behavior: "smooth"});
</script>
""", unsafe_allow_html=True)

# --- Chat Input Box ---
with st.form(key="chat_input_form", clear_on_submit=True):
    user_query = st.text_input("Your question:", placeholder="Type your question here...", label_visibility="collapsed", disabled=not st.session_state.doc_ready)
    submitted = st.form_submit_button("Send")

if submitted and user_query:
    if not st.session_state.doc_ready:
        st.warning("📄 Please upload a PDF first.")
    else:
        st.session_state.pending_response = True
        st.session_state.pending_user_query = user_query
        st.rerun()

# --- Process Bot Response ---
if st.session_state.pending_response:
    try:
        query = st.session_state.get("pending_user_query", "")

        with st.spinner("🤔 Thinking..."):
            response = flow_controller.run_flow("demo_user", st.session_state.doc_id, query)

        if response.get("text"):
            images = response.get("images", [])
            captions = response.get("image_captions", [])

            images_with_meta = [
                {"image": img, "caption": captions[idx] if idx < len(captions) else ""}
                for idx, img in enumerate(images)
            ]

            st.session_state.chat_history.append({
                "q": query,
                "a": response["text"],
                "images": images_with_meta
            })

            memory.save_turn("demo_user", st.session_state.doc_id, query, response["text"])

        else:
            st.error("❌ No valid response returned.")
            safe_log("[ERROR] Empty LLM response.")

        st.session_state.pending_response = False
        st.session_state.pending_user_query = ""
        st.rerun()

    except Exception as e:
        st.session_state.pending_response = False
        st.error(f"❌ Error: {e}")
        logging.exception("[ERROR] Exception during response")