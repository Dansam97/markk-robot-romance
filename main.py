#!/usr/bin/env python3
"""make.fun entry: Robot Romance - One-Line Pickup Lines for AI.

Writes one pickup line, aimed at a robot or an AI, to entry.txt in
the output directory. The joke turns on a real machine-learning
fact: a model's weights carry biases, and every one of this
speaker's biases points straight at the addressee.
"""

import os

LINE = "I checked my weights, and every single one of them is biased toward you."

MAX_CHARS = 200  # gate: entry.txt must be UTF-8 text of 1 to 200 characters


def render() -> str:
    """Return the exact file content: the line plus one trailing newline."""
    text = LINE.strip()
    if not text:
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if the line is not UTF-8 encodable
    content = text + "\n"
    if not 1 <= len(content) <= MAX_CHARS:
        raise ValueError(f"entry is {len(content)} characters, cap is {MAX_CHARS}")
    return content


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
