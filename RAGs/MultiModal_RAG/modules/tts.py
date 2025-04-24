"""
Text-to-Speech (TTS) module using ElevenLabs API.
Generates speech audio from text using a predefined voice and model.
"""

from elevenlabs import ElevenLabs
from modules.config import ELEVENLABS_API_KEY
from modules.utils import safe_log

# --- Configuration ---

# Pre-configured ElevenLabs voice and model settings
DEFAULT_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"         # Example: 'Rachel'
DEFAULT_MODEL_ID = "eleven_multilingual_v2"       # High-quality multilingual voice model
DEFAULT_OUTPUT_FORMAT = "mp3_44100_128"           # MP3 at 44.1kHz, 128kbps

# Initialize ElevenLabs client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


# --- Main Function ---

def text_to_audio(text: str) -> bytes:
    """
    Converts input text to audio using ElevenLabs API.

    Args:
        text (str): Text to be converted to speech.

    Returns:
        bytes: MP3 audio bytes. Returns empty bytes on failure or empty input.
    """
    if not text.strip():
        return b""

    try:
        # Stream audio chunks from ElevenLabs API
        audio_stream = client.text_to_speech.convert(
            text=text,
            voice_id=DEFAULT_VOICE_ID,
            model_id=DEFAULT_MODEL_ID,
            output_format=DEFAULT_OUTPUT_FORMAT
        )

        # Concatenate streamed chunks into a single byte buffer
        return b"".join(audio_stream)

    except Exception as e:
        safe_log(f"❌ ElevenLabs TTS failed: {e}")
        return b""