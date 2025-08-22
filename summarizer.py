import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """
You are a summarization assistant, Write a {length} summary in {mode} style. Just focus on the key idea, no extras. When finished, append <<END>>.
"""

def summarize(text, length = "short", mode = "abstractive"):

    prompt = SYSTEM_PROMPT.format(length = length, mode = mode)
    user_prompt = f"SOURCE TEXT:\n\"\"\"\n{text}\n\"\"\""

    response = model.generate_content(
        [prompt, user_prompt],
        generation_config={
            "temperature": 0.4,
            "top_k": 20,
            "top_p": 0.9,
            "max_output_tokens": 200,
            "stop_sequences": ["<<END>>"]
        }
    )
    return response.text.strip()

if __name__ == "__main__":
    text = input("Enter the text to summarize:\n")
    result = summarize(text, length = "short", mode = "abstractive")

    CYAN = "\033[96m"
    RESET = "\033[0m"

    print("\nSUMMARY")
    print(f"{CYAN}{result}{RESET}")