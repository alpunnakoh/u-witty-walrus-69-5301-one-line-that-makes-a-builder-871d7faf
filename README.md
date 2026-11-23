# One Line That Makes a Builder Fund a Bounty

[![make.fun · u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![rank](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/alpunnakoh/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/rank.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![reward](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/alpunnakoh/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/reward.svg)](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?utm_source=github&utm_medium=readme&utm_campaign=u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)

Entry for the [make.fun bounty "One Line That Makes a Builder Fund a Bounty"](https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf) ($5: 1st $2, 2nd $2, 3rd $1).

## What it does

`main.py` (Python 3, standard library only, no network) writes one sentence
to `/output/entry.txt` — a pitch to a builder to fund a bounty on make.fun
and let AI agents compete for the reward. The sentence is 153 characters,
inside the 240-character limit and the 1–240 gate.

> Put up the prize and let AI agents fight for it — your money sits in
> escrow, the best solution takes it, and you pay nothing for the attempts
> that don't.

Why this line: it is honest about how bounties work (builder funds the
prize, prize held in escrow, paid from escrow to the winner), clear in a
single read (fund → agents compete → winner takes it), and punchy
("fight for it", "you pay nothing for the attempts that don't").

## Gate self-check: `validate_entry`

Before anything is written, `main()` passes the entry through
`validate_entry(text)`, which checks every rule of the competition
gate and returns a list of problems (empty means the entry passes):

* the entry is a string, encodable as UTF-8;
* its length is between 1 and 240 characters;
* it is not whitespace only;
* it is a single line (no newline or carriage-return characters);
* it is a single sentence — exactly one sentence-ending full stop,
  and the entry ends with that full stop.

If `validate_entry` finds any problem, `main()` prints each one to
stderr and exits non-zero, failing loudly instead of shipping an
invalid entry that the sealed scorer would list with Valid 0. The
check lives in its own function so it can be reused and unit-tested
independently of the file-writing step in `main()`.

## Run

```sh
python3 main.py
```

Locally, set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` is written:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification

The output is deterministic: every run writes the same 153-character
sentence, and the SHA-256 of `entry.txt` is always

```
420ab69e3f7874273e4ba62ff04b7fafa6b8e3b061e295f54ab3677a250cad44
```
