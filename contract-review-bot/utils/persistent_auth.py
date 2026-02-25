import json
import os
import secrets

SESSIONS_FILE = "auth_sessions.json"

def _load_sessions():
    if not os.path.exists(SESSIONS_FILE):
        return {}
    try:
        with open(SESSIONS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def _save_sessions(sessions):
    with open(SESSIONS_FILE, "w") as f:
        json.dump(sessions, f)

def create_session(email: str) -> str:
    """Creates a cryptographically secure session token for the user."""
    sessions = _load_sessions()
    
    token = secrets.token_urlsafe(32)
    
    sessions[token] = email
    _save_sessions(sessions)
    
    return token

def validate_session(token: str) -> str:
    """Returns the associated email if valid, or None if invalid/expired."""
    if not token:
        return None
    sessions = _load_sessions()
    return sessions.get(token)

def destroy_session(token: str):
    """Removes the session token from the backend store."""
    if not token:
        return
    sessions = _load_sessions()
    if token in sessions:
        del sessions[token]
        _save_sessions(sessions)