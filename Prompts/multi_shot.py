from summarizer import run_prompt

SYSTEM_PROMPT = """
You are a summarization assistant. Write a {length} summary in {mode} style. 

Here are some examples:

SOURCE: "Climate change is increasing global temperatures."
SUMMARY: "Climate change is raising global temperatures." <<END>>

SOURCE: "Artificial Intelligence is transforming industries by automating tasks."
SUMMARY: "AI automates tasks and transforms industries." <<END>>

SOURCE: "The internet connects people across the world."
SUMMARY: "The internet enables global connectivity." <<END>>

Now summarize the following:
"""

def summarize_multi_shot(text, length="short", mode="abstractive"):
    prompt = SYSTEM_PROMPT.format(length=length, mode=mode)
    user_prompt = f"SOURCE TEXT:\n\"\"\"\n{text}\n\"\"\""
    return run_prompt(prompt, user_prompt)
