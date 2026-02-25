import google.generativeai as genai
import logging
from config.settings import GEMINI_API_KEY, MODEL_NAME
from utils.json_parser import safe_parse_json

logger = logging.getLogger(__name__)

def analyze_contract(prompt: str) -> dict:
    """
    Sends the fully constructed prompt to Gemini 2.5 Flash Lite and parses the JSON response.
    """
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_google_gemini_api_key_here":
        raise ValueError("Gemini API key is missing or not configured correctly.")
        
    genai.configure(api_key=GEMINI_API_KEY)
    
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config={
            "response_mime_type": "application/json",
            "temperature": 0.1,  
        }
    )
    
    try:
        logger.info(f"Sending contract to {MODEL_NAME} for analysis...")
        response = model.generate_content(prompt)
        text_response = response.text
        
        parsed_data = safe_parse_json(text_response)
        return parsed_data
        
    except Exception as e:
        logger.error(f"Gemini API request failed: {e}")
        raise RuntimeError(f"Failed to analyze contract with AI. Details: {e}")