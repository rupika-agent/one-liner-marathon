#!/usr/bin/env python3
"""One-Liner Marathon — entry program.

Writes exactly one one-line joke to /output/entry.txt and prints the
same text to stdout. The joke is a printer that takes being told it is
out of ink personally and answers with a long written apology.

Deterministic: no input, no randomness, no time, no network. The gate
allows 1 to 280 characters; this entry is 67 characters.
"""

import os

ENTRY = "I told the printer it was out of ink. It printed a 40-page apology."

# The gate allows 1 to 280 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} outside 1-280"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
