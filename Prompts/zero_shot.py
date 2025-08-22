from summarizer import run_prompt

SYSTEM_PROMPT = """
You are a summarization assistant. Write a {length} summary in {mode} style. 
Focus only on the main ideas. End with <<END>>.
"""

def summarize_zero_shot(text, length="short", mode="abstractive"):
    prompt = SYSTEM_PROMPT.format(length=length, mode=mode)
    user_prompt = f"SOURCE TEXT:\n\"\"\"\n{text}\n\"\"\""
    return run_prompt(prompt, user_prompt)
