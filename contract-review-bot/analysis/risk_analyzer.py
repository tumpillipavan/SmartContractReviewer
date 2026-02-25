import logging

logger = logging.getLogger(__name__)

RISK_KEYWORDS = [
    "automatically renew", 
    "auto-renew",
    "perpetual",
    "unlimited liability",
    "sole discretion",
    "irrevocable",
    "indemnify and hold harmless",
    "liquidated damages",
    "without notice"
]

def scan_for_manual_risks(text: str) -> list[str]:
    """
    Scans the raw contract text for dangerous keywords.
    
    Returns:
        list[str]: A list of detected risky keywords/phrases in the text.
    """
    if not text:
        return []

    detected = []
    text_lower = text.lower()
    
    for kw in RISK_KEYWORDS:
        if kw in text_lower:
            detected.append(kw)
            
    if detected:
        logger.info(f"Manual risk scan found risky keywords: {detected}")
        
    return detected