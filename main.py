#!/usr/bin/env python3
"""Last Text at One Percent — entry program.

Writes the final text message a phone sends at one percent battery to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

# The phone's last text: a confession it never gets to finish.
SMS = (
    "ok i'm at 1% so listen fast: i've screenshotted every typo "
    "you've made since 2021. the folder is called\u2014"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SMS)
    print(f"wrote {len(SMS)} characters to {path}")


if __name__ == "__main__":
    main()
