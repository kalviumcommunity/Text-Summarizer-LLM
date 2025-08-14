# run_summary.py
from summarizer import summarize_text

def main():
    print("=== Gemini 2.0 Text Summarizer ===")
    text = input("Enter your text: ")
    summary_type = input("Summary type (short/detailed, default=short): ") or "short"

    summary = summarize_text(text, summary_type)
    print("\n=== Summary ===")
    print(summary)

if __name__ == "__main__":
    main()
