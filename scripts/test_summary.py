# test_summary.py
import os
from summarizer import summarize_text
from utils import clean_text

RAW_DIR = "data/raw/"

def summarize_files(summary_type="short"):
    for filename in os.listdir(RAW_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(RAW_DIR, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            
            print(f"\n--- Summarizing: {filename} ---\n")
            summary = summarize_text(text, summary_type)
            print(summary)
            print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    # Change to "detailed" for paragraph-style summaries
    summarize_files(summary_type="short")
