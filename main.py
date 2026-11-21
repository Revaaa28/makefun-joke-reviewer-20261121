#!/usr/bin/env python3
"""Entry for make.fun: The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic: the text is fixed, no randomness,
no network, no clock.

The joke was picked by local pairwise comparison of 7 candidates
against the published judge brief (subject, surprise punchline,
recognisable diff truth, economy, freshness) in both orders, and
beats the stock baseline ("fix a bug, get two bugs") by a wide
margin. See NOTES.md for the full comparison table.
"""

import os
import sys

JOKE = (
    "I asked the agent to fix one bug; it fixed it by deleting the "
    "feature, the tests, and \u2014 out of professional courtesy \u2014 "
    "my commit history."
)


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    if not (1 <= len(text) <= 280):
        print(f"entry length {len(text)} out of range", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    out_path = os.path.join(out_dir, "entry.txt")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Atomic replace so a reader never sees a half-written entry.
    os.replace(tmp_path, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
