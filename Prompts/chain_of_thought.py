from summarizer import run_prompt

SYSTEM_PROMPT = """
You are a summarization assistant. Write a {length} summary in {mode} style.
Before giving the summary, think step by step about the key points. End your reasoning with <<END>> and then give the final summary.
"""

def summarize_chain_of_thought(text, length="short", mode="abstractive"):
    prompt = SYSTEM_PROMPT.format(length=length, mode=mode)
    user_prompt = f"SOURCE TEXT:\n\"\"\"\n{text}\n\"\"\""
    return run_prompt(prompt, user_prompt)
