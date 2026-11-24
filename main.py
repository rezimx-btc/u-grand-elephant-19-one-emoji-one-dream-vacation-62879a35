#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry writer.

Writes the chosen emoji to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.

Chosen entry: 🏝️ (desert island).
Candidates considered, each a different winning structure:
  1. 🏝️ — one concrete object (X2): the island itself, the universal
     dream-vacation icon. No explanation, no setup.
  2. 🧳 — implied second person (X1): a packed suitcase — not a place,
     but YOU about to leave; the judge sees themselves departing.
  3. 🌅 — twist/shape (X3): sunrise over the sea — the dream as a
     moment (the first morning of the trip), not a place or a thing.
🏝️ wins: it hits X2 (one concrete object), X3 (structure: one perfect
place, zero noise — the shape of a dream), X4 (exactly one emoji,
maximum length discipline) and X5 (instantly legible as "dream
vacation" in a single screen pass — the desert island is the canonical
visual shorthand). 4 of 5 patterns. X1 is not literally reachable in a
single emoji, though the empty island invites the viewer to put
themselves on it.
"""

import os

ENTRY = "\U0001f3dd\ufe0f"  # 🏝️ desert island — the dream vacation


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
