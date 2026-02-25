import json
import os
import hashlib
import logging

logger = logging.getLogger(__name__)

DB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
if not os.path.exists(DB_DIR):
    try:
        os.makedirs(DB_DIR)
    except Exception as e:
        logger.error(f"Could not create data directory: {e}")

USERS_FILE = os.path.join(DB_DIR, "users.json")

def _hash_password(password: str) -> str:
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users() -> dict:
    """Loads users from the JSON database."""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load user DB: {e}")
            return {}
    return {}

def save_user(email: str, password: str) -> bool:
    """Registers a new user if the email is unique."""
    users = load_users()
    
    if email in users:
        return False 
    
    users[email] = {
        "password": _hash_password(password)
    }
    
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Failed to save user: {e}")
        return False

def verify_credentials(email: str, password: str) -> bool:
    """Verifies user credentials."""
    users = load_users()
    
    if email not in users:
        return False
    
    return users[email]["password"] == _hash_password(password)