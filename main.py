#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is a GPS with a
direction problem: it can only turn left at puns, and it has been
driving straight for years.
"""

import os

JOKE = (
    "I asked my GPS to tell me a joke. "
    "It said, 'Turn left at the next pun \u2014 "
    "you've been driving straight for years.'"
)


def main() -> None:
    # The sealed scorer gates /output/entry.txt at 1-200 characters;
    # refuse to write anything outside the gate rather than ship it.
    assert 1 <= len(JOKE) <= 200, "joke outside the 1-200 character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
