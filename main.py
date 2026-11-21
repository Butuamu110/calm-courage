#!/usr/bin/env python3
"""Calm Courage — entry for make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text (angle: "The Shore", an A1 'Ground & Weight' sea
variant) to /output/entry.txt. The sea does the calming: it never hurries,
it has never been late, and what you need is already coming toward you —
courage shown, never commanded.
"""

import os

TEXT = "The sea does not hurry to the shore, and it has never once been late. It comes the way breath comes to a sleeping house — in, and in again, each time a little braver. Stand where the water can reach you. You do not have to chase what is already coming."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
