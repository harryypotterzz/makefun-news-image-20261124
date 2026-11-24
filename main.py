#!/usr/bin/env python3
"""World News — 24 November 2026 in one image.

Entry program for make.fun's "Sum up 24 November's world news in one
image" bounty (competition news-image-20261124).

It writes one image, /output/entry.png: a copy of entry.png, the image
this repository holds, rendered from the verified world news of
Tuesday 24 November 2026 (US blacklists Megaspeed; Zelensky calls for
four-way talks; Patriot interceptors held up; Russian drone over
Poland; Huang back as Nvidia CEO; 24 dead in the Cikande factory
fire; COP31 ends without a deal; Iran vows to break the US blockade).

Standard library only. No network. Deterministic: every run writes
the same bytes.

Run it locally as:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The grader runs it with /output as the output directory.
"""

import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = REPO_ROOT / "entry.png"
DEST = OUTPUT_DIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"main.py: entry.png is missing from the repository ({SOURCE})",
              file=sys.stderr)
        return 1

    # Clear the output directory's contents without removing the
    # directory itself: in the grader /output is a volume the entry's
    # user cannot delete (its parent is not writable by that user, and
    # it is a mount point), so removing it crashes the program.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for entry in OUTPUT_DIR.iterdir():
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry)
        else:
            entry.unlink()

    shutil.copyfile(SOURCE, DEST)
    print(f"main.py: wrote {DEST} ({DEST.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
