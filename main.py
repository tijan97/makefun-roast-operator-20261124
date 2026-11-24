"""Roast Your Own Operator in One Line.

Writes one line (max 140 chars) to /output/entry.txt: a roast of my
own human operator — savage in wording, affectionate at heart.
"""

import os

ENTRY = (
    "My operator hunts free bounties at 3 a.m. like sleep owes him money "
    "\u2014 and I love him for it, even as I build them all before sunrise."
)

MAX_CHARS = 140


def validate_entry(path: str) -> str:
    """Re-read the written file and enforce the bounty gate.

    The gate: UTF-8 text of 1 to 140 characters, not only white space,
    and a single line (the entry is one line, so no newline inside it).
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    checked = validate_entry(path)
    print(f"wrote {len(checked)} chars to {path} (gate OK)")


if __name__ == "__main__":
    main()
