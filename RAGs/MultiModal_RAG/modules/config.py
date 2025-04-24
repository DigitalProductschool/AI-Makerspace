"""
Configuration loader module.
Loads API keys and runtime variables from a `.env` file for secure, centralized access.
"""

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Template to guide missing variables
ENV_TEMPLATE_HINT = """
Example .env file:

OPENAI_API_KEY=your-openai-api-key-here
TOGETHER_API_KEY=your-together-api-key-here
LLAMAPARSE_API_KEY=your-llamaparse-api-key-here
MEM0_API_KEY=your-mem0-api-key-here
ELEVENLABS_API_KEY=your-elevenlabs-api-key-here
ACTIVE_PROVIDER=together  # or openai
"""

def get_env_var(key: str, required: bool = True, default: str = None) -> str:
    """
    Fetches an environment variable and validates its presence if required.

    Args:
        key (str): Environment variable name.
        required (bool): Whether to raise an error if the key is missing.
        default (str): Fallback value if the variable is optional.

    Returns:
        str: The environment variable value.

    Raises:
        ValueError: If required and not found.
    """
    value = os.getenv(key, default)
    if required and not value:
        raise ValueError(
            f"❌ Missing required environment variable: {key}\n"
            f"Please set it in your `.env` file.\n\n{ENV_TEMPLATE_HINT}"
        )
    return value

# --- Memory: Mem0 ---
MEM0_API_KEY = get_env_var("MEM0_API_KEY")

# --- PDF Parsing: LlamaParse ---
LLAMAPARSE_API_KEY = get_env_var("LLAMAPARSE_API_KEY")

# --- LLM Access ---
OPENAI_API_KEY = get_env_var("OPENAI_API_KEY")
TOGETHER_API_KEY = get_env_var("TOGETHER_API_KEY")
ACTIVE_PROVIDER = os.getenv("ACTIVE_PROVIDER", "together")
TOGETHER_CHAT_COMPLETIONS_URL = os.getenv(
    "TOGETHER_CHAT_COMPLETIONS_URL",
    "https://api.together.xyz/v1/chat/completions"
)

# --- Text-to-Speech: ElevenLabs ---
ELEVENLABS_API_KEY = get_env_var("ELEVENLABS_API_KEY")