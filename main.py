from Prompts.zero_shot import summarize_zero_shot
from Prompts.one_shot import summarize_one_shot

CYAN = "\033[96m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def main():
    print(f"\n{GREEN}=== Text Summarizer using LLMs ==={RESET}")
    
    choice = input("Choose prompting method (zero / one): ").strip().lower()
    
    text = input("\nEnter the text to summarize:\n")
    
    length = "detailed"
    mode = input(f"\n{RED}Enter a type / mode of summarization:{RESET} ").lower().strip()

    if choice == "zero":
        result = summarize_zero_shot(text, length, mode)
    elif choice == "one":
        result = summarize_one_shot(text, length, mode)
    else:
        print("Invalid choice. Try again.")
        return

    print("\nSummary")
    print("================================================================================================================================================================================================")
    print(f"{CYAN}{result}{RESET}")

if __name__ == "__main__":
    main()
