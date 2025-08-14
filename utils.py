# utils.py
import re

def clean_text(text: str) -> str:
    """
    Clean input text by removing extra spaces, newlines, and unnecessary characters.
    
    Args:
        text (str): Raw input text
    
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text
