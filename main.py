import sys
import os
from summarization.preprocess import clean_text
from summarization.summarizer import summarize

# Ensure Python uses UTF-8 for stdout on Windows terminals
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        os.environ.setdefault("PYTHONIOENCODING", "utf-8")

with open("data/input.txt", "r", encoding="utf-8") as file:
    text = file.read()

cleaned_text = clean_text(text)

summary = summarize(cleaned_text)

print("ORIGINAL TEXT:\n")
print(text)

print("\nSUMMARY:\n")
print(summary)

# Fallback: also write summary to a UTF-8 file so Tamil is preserved
out_path = os.path.join("data", "output.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("ORIGINAL TEXT:\n")
    f.write(text + "\n\n")
    f.write("SUMMARY:\n")
    f.write(summary + "\n")
