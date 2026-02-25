import google.generativeai as genai
import streamlit as st
from config.settings import GEMINI_API_KEY, MODEL_NAME

def is_api_configured() -> bool:
    """
    Checks if the Gemini API key is configured.
    """
    return bool(GEMINI_API_KEY and GEMINI_API_KEY.strip() and GEMINI_API_KEY != "your_google_gemini_api_key_here")

def check_api_connection() -> bool:
    """
    Attempts to list models to verify the API key is active.
    """
    if not is_api_configured():
        return False
        
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        genai.get_model(f"models/{MODEL_NAME}")
        return True
    except Exception:
        return False

@st.cache_data(ttl=600, show_spinner=False)
def ping_gemini_api() -> bool:
    """
    Performs a minimal generation request to verify actual quota/auth status.
    """
    if not is_api_configured():
        return False
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        genai.get_model(f"models/{MODEL_NAME}")
        return True
    except Exception:
        return False