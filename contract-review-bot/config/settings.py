import os
from dotenv import load_dotenv

load_dotenv(override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-flash-latest"

APP_NAME = "AI Contract Intelligence Platform"
CONFIDENCE_WARNING_THRESHOLD = 60
CONFIDENCE_ERROR_THRESHOLD = 40