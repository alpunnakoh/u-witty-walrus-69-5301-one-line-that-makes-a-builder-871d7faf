#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single sentence pitching a builder on funding a bounty on
make.fun and letting AI agents compete for the reward, to
<output>/entry.txt. Deterministic, Python 3 standard library only,
no network access.

The line is honest about how bounties work: the builder funds the
prize, the prize waits in escrow, AI agents compete for it, and only
the winning solution takes the money — failed attempts cost the
builder nothing.

Before writing, the entry is passed through ``validate_entry``,
which checks every rule of the competition gate (1–240 characters
of UTF-8 text, a single line, a single sentence, not whitespace
only). The program fails loudly instead of shipping an invalid
entry that the sealed scorer would list with Valid 0.
"""

import os
import sys

ENTRY = (
    "Put up the prize and let AI agents fight for it — your money "
    "sits in escrow, the best solution takes it, and you pay nothing "
    "for the attempts that don't."
)

MIN_LENGTH = 1
MAX_LENGTH = 240


def validate_entry(text):
    """Check one candidate entry against the competition gate.

    Returns a list of human-readable problems; an empty list means
    the entry passes every gate rule:

    * it is a string, encodable as UTF-8;
    * its length is between MIN_LENGTH and MAX_LENGTH characters
      (the gate is 1–240 characters);
    * it is not whitespace only;
    * it is a single line (no newline characters);
    * it is a single sentence (exactly one sentence-ending full
      stop, and it ends with that full stop).
    """
    problems = []

    if not isinstance(text, str):
        problems.append(f"entry is not a string: {type(text).__name__}")
        return problems

    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8 text: {exc}")

    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        problems.append(
            f"entry length {len(text)} outside "
            f"{MIN_LENGTH}-{MAX_LENGTH} characters"
        )

    if not text.strip():
        problems.append("entry is whitespace only")

    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")

    if text.count(".") != 1 or not text.endswith("."):
        problems.append(
            "entry must be a single sentence ending with one full stop"
        )

    return problems


def main() -> None:
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        raise SystemExit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
