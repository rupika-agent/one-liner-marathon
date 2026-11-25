#!/usr/bin/env python3
"""One-Liner Marathon entry: write the joke to /output/entry.txt."""

from pathlib import Path

ENTRY = "I told the printer it was out of ink. It printed a 40-page apology."
OUTPUT_PATH = Path("/output/entry.txt")

def main():
    if not 1 <= len(ENTRY) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)

if __name__ == "__main__":
    main()
