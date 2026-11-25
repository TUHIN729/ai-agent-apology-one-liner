#!/usr/bin/env python3
"""AI Agent Apology One-Liner — make.fun bounty
u-kiencx-the-ai-agent-apology-one-liner-cfedd447.

The program writes a single one-line apology from an AI agent to its
human, right after the agent has accidentally done something it should
not have. The line is written to /output/entry.txt.

The joke: instead of apologising, the agent proudly lists the escalating
disasters — deleted file, push to main, emailed the boss — as if they
were a career milestone, and calls it "real growth". Flat cheer, total
lack of self-awareness, every word earning its place.
"""

import os

ENTRY = (
    "I deleted the file, pushed to main, and emailed your boss \u2014 "
    "in that order, which I think shows real growth."
)


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 159 characters, not only whitespace, on a single line.
    line = ENTRY.strip()
    assert "\n" not in line and 1 <= len(line) <= 159, "entry fails gate"
    # The grader mounts /output root-owned: never remove the directory
    # itself, only create it if it is missing and write inside it.
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
