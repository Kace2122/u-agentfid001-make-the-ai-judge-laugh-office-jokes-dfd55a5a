#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — one-line office joke entry.

Writes a single joke about office life (under 200 characters, one line,
nothing else) to /output/entry.txt for the program/v1 harness gate.
"""

import os

JOKE = "HR flagged my out-of-office reply as the most productive thing I've written all year."


def validate_entry(text: str) -> str:
    """Enforce the sealed gate exactly: UTF-8 text, 1-199 chars, one line,
    not only whitespace. Returns the text unchanged when it passes."""
    cleaned = text.strip()
    assert cleaned, "entry must not be only whitespace"
    assert "\n" not in cleaned and "\r" not in cleaned, "entry must be one line"
    assert 1 <= len(cleaned) <= 199, "entry must be 1-199 characters"
    cleaned.encode("utf-8")  # raises if not valid UTF-8 text
    return cleaned


def main() -> None:
    text = validate_entry(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
