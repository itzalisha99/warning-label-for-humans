#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label for human beings to
/output/entry.txt. Standard library only, deterministic.
"""

import os

LABEL = "WARNING: This human contains traces of nuts, grudges, and unread emails from 2019."


def validate(text: str) -> None:
    """Mirror the house gate: fail loudly instead of writing an invalid entry."""
    if not (1 <= len(text) <= 160):
        raise ValueError(f"label is {len(text)} characters, must be 1-160")
    if text != text.strip() or not text.strip():
        raise ValueError("label must be non-blank with no leading/trailing space")
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    text.encode("utf-8")  # raises if not encodable


def main() -> None:
    validate(LABEL)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
