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
"""

import os

ENTRY = (
    "Put up the prize and let AI agents fight for it \u2014 your money "
    "sits in escrow, the best solution takes it, and you pay nothing "
    "for the attempts that don't."
)


def main() -> None:
    # Self-check against the competition gate before writing: the entry
    # must be 1-240 characters of UTF-8 text, a single sentence, and not
    # whitespace only. Fail loudly here instead of shipping an invalid
    # entry that the sealed scorer would list with Valid 0.
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} outside 1-240"
    assert ENTRY.strip(), "entry is whitespace only"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
