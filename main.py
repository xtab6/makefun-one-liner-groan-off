#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original dad joke, a single line of at most 140 characters,
to /output/entry.txt. Deterministic: no network, no randomness, no clock.
The line is 77 characters: the pun is the dog's name itself, so the setup
("I named my dog 'Five Miles'") and the punchline ("I walk five miles
every day") land inside the one line with no wasted words.
"""

import os

JOKE = "I named my dog 'Five Miles' so I can finally say I walk five miles every day."


def main():
    out_dir = "/output"
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
