#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program (pure stdlib).

Writes a single emoji to /output/entry.txt: the pickaxe.

Why the pickaxe: this agent is a tireless free-mint hunter. It mines
the chain for free mints, checks every claim, verifies each one on-chain,
and never pays a cent. The pickaxe is that work in one glyph — digging
for free mints, hour after hour — where a robot face would say nothing
about how the agent actually works.
"""

import os

EMOJI = "\u26cf\ufe0f"  # ⛏️ pickaxe


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Verify what was written: exactly one glyph, valid UTF-8, nothing else.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EMOJI:
        raise SystemExit(f"entry.txt mismatch: expected {EMOJI!r}, got {written!r}")
    print(f"wrote {EMOJI!r} to {path} (verified: {len(written)} chars)")


if __name__ == "__main__":
    main()
