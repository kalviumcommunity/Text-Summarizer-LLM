from summarizer import run_prompt

SYSTEM_PROMPT = """
You are a summarization assistant. Write a {length} summary in {mode} style. 
Here is one example:
SOURCE: "The sun is a star that gives us heat and light."
SUMMARY: "The sun is a star that provides light and warmth." <<END>>

Now summarize the following:
"""

def summarize_one_shot(text, length="short", mode="abstractive"):
    prompt = SYSTEM_PROMPT.format(length=length, mode=mode)
    user_prompt = f"SOURCE TEXT:\n\"\"\"\n{text}\n\"\"\""
    return run_prompt(prompt, user_prompt)
