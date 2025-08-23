import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

def run_prompt(system_prompt, user_prompt, config=None):
    """Runs the prompt with given config and returns text"""
    if config is None:
        config = {
            "temperature": 0.9,     # From 0.1 to 0.9, tells the AI on how random / creative the result has to be.
            "top_k": 20,
            "top_p": 0.9,
            "max_output_tokens": 400,
            "stop_sequences": ["<<END>>"]
        }

    response = model.generate_content(
        [system_prompt, user_prompt],
        generation_config=config
    )
    return response.text.strip()
