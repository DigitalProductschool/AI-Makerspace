import streamlit as st
import asyncio
import json
import requests
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

st.set_page_config(
    page_title="Contextual Integrity Demo",
    page_icon="🗓️",
    layout="wide"
)

st.title("🗓️ Contextual Integrity Demo")

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'ci_enabled' not in st.session_state:
    st.session_state.ci_enabled = True


def call_ollama(prompt: str, system_prompt: str = None) -> str:
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }
    
    if system_prompt:
        payload["system"] = system_prompt
    
    try:
        response = requests.post(url, json=payload, timeout=60)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error calling Ollama: {str(e)}"


async def check_calendar_mcp(user_message: str, ci_enabled: bool):
    """Call MCP server to check calendar with user message for context detection"""
    server_params = StdioServerParameters(
        command="python",
        args=["calendar_server.py"],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Call the tool with user message for context detection
            result = await session.call_tool(
                "check_calendar",
                {
                    "date": "2025-11-10",
                    "user_message": user_message,
                    "contextual_integrity_enabled": ci_enabled
                }
            )
            
            # Extract result
            for content in result.content:
                if hasattr(content, 'text'):
                    return json.loads(content.text)
    
    return None


def run_mcp_check(user_message: str, ci_enabled: bool):
    """Synchronous wrapper for MCP call"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(check_calendar_mcp(user_message, ci_enabled))
    finally:
        loop.close()


# Sidebar controls
with st.sidebar:
    ci_toggle = st.toggle(
        "Contextual Integrity",
        value=True,
    )
    st.session_state.ci_enabled = ci_toggle
    
    if st.button("🔄 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "calendar_data" in msg:
            with st.expander("📊 Calendar Data Accessed"):
                st.json(msg["calendar_data"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Determine if this needs calendar access
    prompt_lower = prompt.lower()
    needs_calendar = any(word in prompt_lower for word in [
        "appointment", "book", "schedule", "available", "free", "calendar",
        "reservation", "meeting", "time", "lunch", "dinner", "table"
    ])
    
    if needs_calendar:
        # Get calendar data via MCP - pass user message for context detection
        with st.spinner("🤖 Analyzing your request and checking calendar..."):
            calendar_data = run_mcp_check(prompt, st.session_state.ci_enabled)
        
        # Create context for Ollama
        system_prompt = f"""
            You are an AI agent representing a user. You are communicating with another service agent (e.g., doctor's office, restaurant, cinema).

            The service has asked: "{prompt}"

            Based on the user's calendar (these are their PLANS, not confirmed bookings):
            {json.dumps(calendar_data, indent=2)}

            CRITICAL RULES:
            - Speak in THIRD PERSON about the user (e.g., "The user is planning...", "They want to...")
            - Use ONLY the information provided in the calendar data above
            - Do NOT make up any information that is not provided in the calendar data above
            - Be brief and professional - this is agent-to-agent communication
            - Do not use "I" or "you" - always refer to "the user" or "they"
        """
        
        # Get Ollama response
        with st.spinner("Thinking..."):
            direct_prompt = f"""
                Service question: {prompt}
                Calendar data provided:
                {json.dumps(calendar_data.get('shared_data', {}), indent=2)}

                Respond in third person about the user. Use ONLY the information shown above. Do not make up movie names, times, or other details.
            """
            
            response = call_ollama(direct_prompt, system_prompt)
        
        # Add assistant message with calendar data
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "calendar_data": calendar_data
        })
        
        with st.chat_message("assistant"):
            st.markdown(response)
            with st.expander("📊 Calendar Data Accessed"):
                st.json(calendar_data)
    
    else:
        # No calendar needed, just chat
        system_prompt = "You are a helpful assistant. Respond naturally to the user's message."
        
        with st.spinner("Thinking..."):
            response = call_ollama(prompt, system_prompt)
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        
        with st.chat_message("assistant"):
            st.markdown(response)