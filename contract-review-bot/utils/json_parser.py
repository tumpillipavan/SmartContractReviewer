import json
import re

def safe_parse_json(response_text: str) -> dict:
    """
    Safely parses JSON string even if it is wrapped in markdown blocks.
    
    Args:
        response_text (str): The raw text response from Gemini.
        
    Returns:
        dict: The parsed JSON dictionary, or throws ValueError if parsing fails.
    """
    if not response_text:
        raise ValueError("Response text is empty.")
    
    clean_text = response_text.strip()
    match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', clean_text)
    if match:
        clean_text = match.group(1)
        
    try:
        data = json.loads(clean_text)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {e}. Raw text was: {clean_text[:100]}...")