import streamlit as st
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def handle_exceptions(message="An error occurred."):
    """
    A decorator to catch exceptions, log them, and show a user-friendly error in Streamlit.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_details = str(e)
                logger.error(f"Error in {func.__name__}: {error_details}")
                st.error(f"🚨 {message}")
                with st.expander("View Error Details"):
                    st.code(error_details)
                return None
        return wrapper
    return decorator