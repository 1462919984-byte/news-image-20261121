#!/usr/bin/env python3
"""Entry point for the news-image-20261121 bounty (v5).

The grader expects one image at /output/entry.png. This repository
already holds that image as entry.png: a newspaper front page that
sums up the world news of Saturday 21 November 2026. Running this
script copies the image into place. It touches no network and
produces identical bytes on every run.

To check locally without writing to /output, set MAKEFUN_OUTPUT_DIR
to any directory; the script will put entry.png there instead.
"""

import os
import pathlib
import shutil


def repo_root() -> pathlib.Path:
    """Directory holding this script (and entry.png)."""
    return pathlib.Path(__file__).resolve().parent


def resolve_output_dir() -> pathlib.Path:
    """Where the grader wants the image.

    Defaults to /output; MAKEFUN_OUTPUT_DIR overrides it so the
    entry can be checked locally without touching /output.
    """
    return pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def place_image() -> pathlib.Path:
    """Copy entry.png from this repo into the grader's output dir.

    The grader runs the program twice with no network and compares
    the two outputs byte for byte, so the copy must be exact: after
    writing, the target's size is checked against the source and a
    mismatch fails loudly instead of shipping a truncated image.
    """
    repo_dir = repo_root()
    source = repo_dir / "entry.png"
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError(f"copied image is incomplete: {target}")
    return target


def main() -> int:
    placed = place_image()
    print(f"entry placed at {placed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
