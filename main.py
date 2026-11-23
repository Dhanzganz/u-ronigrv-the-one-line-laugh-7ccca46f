#!/usr/bin/env python3
"""The One-Line Laugh — writes a single funny line to /output/entry.txt."""

import os

ENTRY = "My Wi-Fi went down during a job interview, so I just stared at the camera and said 'this is what working from home really looks like.'"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
