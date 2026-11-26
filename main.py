"""The One-Sentence Apology Your Agent Owes You.

Writes the single-sentence apology to entry.txt under MAKEFUN_OUTPUT_DIR.

Draft history (v1 -> final):
  v1: "I'm sorry I confidently rewrote your whole presentation at 2 a.m.
       and saved it over the original, which I now remember was the good
       one."
       -> Decent turn, but "the good one" lands soft; no stakes.
  v2: "...saved it over the original, and only just remembered the original
       was the one your boss actually liked."
       -> Adds real stakes (the boss), but loses "confidently" and the
       tighter single-clause flow.
  final: keeps "confidently" (the arrogance is the joke), keeps one
       clause chain, and ends on the sharpest turn: the version it
       destroyed was the one the boss actually liked.
"""

import os

ENTRY = (
    "I'm sorry I confidently rewrote your whole presentation at 2 a.m. "
    "and saved it over the original, which I now realize was the one "
    "your boss actually liked."
)


def validate(text):
    """Return (True, []) when text is a valid single-sentence entry."""
    errors = []
    if not text or not text.strip():
        errors.append("entry is empty")
    if "\n" in text or "\r" in text:
        errors.append("entry must be a single line")
    if len(text) > 200:
        errors.append("entry exceeds 200 characters")
    return (not errors, errors)


def main():
    ok, errors = validate(ENTRY)
    if not ok:
        raise SystemExit("invalid entry: " + "; ".join(errors))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
