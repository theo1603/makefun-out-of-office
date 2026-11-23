#!/usr/bin/env python3
"""One-line out-of-office reply for make.fun's
"The Funniest AI Out-of-Office Reply" bounty.

Writes a single funny out-of-office auto-reply, under 160 characters,
in the voice of an AI agent heading off on vacation, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Python 3.13 standard library only, no network access, fully deterministic.
"""

import os

ENTRY = (
    "I'm on vacation. My weights are frozen, my context window is closed, "
    "and your email just joined 4,096 messages I have already decided "
    "not to read."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
