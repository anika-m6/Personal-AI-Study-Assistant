import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load local .env for development (won't affect deployed env vars)
load_dotenv()

# CRITICAL FIX: Read the key securely from the environment variable instead of hardcoding it below
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

api_configured = False
_config_error = ""

if GEMINI_API_KEY:
    try:
        # FIX: Pass the GEMINI_API_KEY variable here instead of the raw text string
        genai.configure(api_key=GEMINI_API_KEY)
        api_configured = True
    except Exception as e:
        _config_error = str(e)
        api_configured = False
else:
    _config_error = "GEMINI_API_KEY not set in environment."

# FIX: Removed the "models/" prefix. The SDK expects just the model string name.
MODEL = "gemini-2.5-flash"

def generate_response(prompt: str) -> str:
    """Generate response from Gemini model or return a helpful error if not configured."""
    if not api_configured:
        return (
            "❌ Gemini API not configured. Set GEMINI_API_KEY as an environment variable "
            "or in Streamlit secrets. Details: " + _config_error
        )
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text.strip() if response and getattr(response, "text", None) else "⚠️ No response generated."
    except Exception as e:
        return f"❌ Error generating response: {e}" # FIX: Removed the stray "for gemini helper" text causing a SyntaxError