from Prompts.zero_shot import summarize_zero_shot
from Prompts.one_shot import summarize_one_shot
from Prompts.multi_shot import summarize_multi_shot
from Prompts.chain_of_thought import summarize_chain_of_thought

def generate_summary(choice: str, text: str, mode: str):
    length = "detailed"
    choice = choice.lower().strip()

    if choice == "zero":
        return summarize_zero_shot(text, length, mode)
    elif choice == "one":
        return summarize_one_shot(text, length, mode)
    elif choice == "multi":
        return summarize_multi_shot(text, length, mode)
    elif choice == "chain":
        return summarize_chain_of_thought(text, length, mode)
    else:
        return "Invalid choice."
