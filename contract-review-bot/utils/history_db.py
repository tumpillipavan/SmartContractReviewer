import json
import os
import logging

logger = logging.getLogger(__name__)

DB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
if not os.path.exists(DB_DIR):
    try:
        os.makedirs(DB_DIR)
    except Exception as e:
        logger.error(f"Could not create data directory: {e}")

HISTORY_FILE = os.path.join(DB_DIR, "session_history.json")

def load_history() -> list:
    """
    Loads the analysis history from local JSON database.
    This acts as our persistent state across hard page refreshes.
    """
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load history DB: {e}")
            return []
    return []

def save_history(history_list: list) -> None:
    """
    Saves the analysis history to local JSON database.
    """
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history_list, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save history DB: {e}")