# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model settings
GEMINI_MODEL = "gemini-2.0-flash"  # or whichever Gemini model you want

# Optional: default summary type
DEFAULT_SUMMARY_TYPE = "short"
