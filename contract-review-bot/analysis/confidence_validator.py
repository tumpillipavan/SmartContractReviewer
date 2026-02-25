import streamlit as st
import logging
from config.settings import CONFIDENCE_WARNING_THRESHOLD, CONFIDENCE_ERROR_THRESHOLD

logger = logging.getLogger(__name__)

def validate_and_display_confidence(confidence_score: int):
    """
    Evaluates the confidence score provided by the AI and displays 
    appropriate Streamlit alerts.
    
    Args:
        confidence_score (int): The 0-100 confidence score from Gemini.
    """
    try:
        score = int(confidence_score)
    except (ValueError, TypeError):
        st.warning("⚠ AI Confidence Score missing or invalid format. Proceed with manual review.")
        return

    logger.info(f"Confidence score evaluated: {score}")

    if score < CONFIDENCE_ERROR_THRESHOLD:
        st.error(f"🚨 Very Low Confidence ({score}/100) — Results may be unreliable. Manual legal review is highly recommended.")
    elif score < CONFIDENCE_WARNING_THRESHOLD:
        st.warning(f"⚠ Low AI Confidence ({score}/100) — Review the extracted key terms carefully.")
    else:
        st.success(f"✅ High AI Confidence ({score}/100) — Extraction appears highly reliable.")