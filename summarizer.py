# summarizer.py
from config import GEMINI_API_KEY, GEMINI_MODEL
from google import genai
from utils import clean_text

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

def summarize_text(text: str, summary_type: str = "short") -> str:
    """
    Summarize input text using Gemini 2.0.

    Args:
        text (str): Input text to summarize.
        summary_type (str): "short" or "detailed"

    Returns:
        str: Summarized text
    """
    if not text.strip():
        return ""

    # Clean the text before sending to LLM
    cleaned_text = clean_text(text)

    # Prepare prompt based on summary_type
    if summary_type == "detailed":
        prompt = f"Summarize the following text in a detailed, paragraph style:\n\n{cleaned_text}"
    else:
        prompt = f"Summarize the following text in concise bullet points:\n\n{cleaned_text}"

    # Call Gemini 2.0 API
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text
