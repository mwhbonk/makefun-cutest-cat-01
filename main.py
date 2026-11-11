#!/usr/bin/env python3
"""cutest-cat-01 entry: write one picture of a cat to /output/entry.png.

The picture is a fluffy white kitten with huge blue eyes and a tiny pink
bow, stored in this repository as base64 text in cat.png.b64 (a single
line, so the repository holds no binary files). The program decodes it
and writes the PNG bytes to /output/entry.png.

No network, no randomness, no timestamps: two runs write the same bytes.
"""

import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "cat.png.b64")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(SRC, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())
    with open(DST, "wb") as out:
        out.write(data)
    print("wrote", DST)


if __name__ == "__main__":
    main()
