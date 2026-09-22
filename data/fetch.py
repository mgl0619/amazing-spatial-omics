"""Fetch the public-tier datasets.

Primary data is never committed. This script is the committed artefact: it pins each
dataset to an accession and verifies a checksum before anything downstream runs.

Usage:
    python data/fetch.py --dataset <name>
    python data/fetch.py --all
"""

import argparse
import hashlib
import pathlib

CACHE = pathlib.Path(__file__).parent / "cache"

# name -> (url, sha256, licence). Every entry needs all three.
DATASETS: dict[str, tuple[str, str, str]] = {
    # "demo_section": ("https://...", "TODO_sha256", "CC-BY-4.0"),
}


def verify(path: pathlib.Path, expected: str) -> None:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    actual = h.hexdigest()
    if actual != expected:
        raise SystemExit(f"checksum mismatch for {path}: {actual} != {expected}")


def fetch(name: str) -> pathlib.Path:
    if name not in DATASETS:
        raise SystemExit(f"unknown dataset: {name}")
    url, sha, licence = DATASETS[name]
    CACHE.mkdir(parents=True, exist_ok=True)
    target = CACHE / name
    if target.exists():
        verify(target, sha)
        return target
    raise SystemExit(
        f"TODO: implement download for {name} from {url} (licence: {licence})"
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    names = list(DATASETS) if args.all else [args.dataset]
    for n in names:
        print(fetch(n))
