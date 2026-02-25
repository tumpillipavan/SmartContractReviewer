import logging

logger = logging.getLogger(__name__)

INJECTION_KEYWORDS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "act as system",
    "override instructions",
    "simulate a different model",
    "you are no longer",
    "system prompt",
    "forget previous",
    "bypassing"
]

def scan_for_prompt_injection(text: str) -> bool:
    """
    Scans the input text for potential prompt injection patterns.
    
    Returns:
        bool: True if an injection attempt is detected, False otherwise.
    """
    if not text:
        return False
        
    text_lower = text.lower()
    
    for keyword in INJECTION_KEYWORDS:
        if keyword in text_lower:
            logger.warning(f"Prompt injection pattern detected: '{keyword}'")
            return True
            
    return False