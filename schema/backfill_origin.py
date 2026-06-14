#!/usr/bin/env python3
"""
v3.0 origin-field backfill.

Adds `metadata.origin: <value>` to every entry in data/beings/.
Default value is `manufactured`. Hand-coded exception list below
captures the non-default cases identified in the v3.0 design pass.

The insertion is positioned in the YAML file immediately after the
`substrate:` block, matching the order declared in
`schema/cb-schema.yaml`. The script preserves all other formatting.

Idempotent: re-running on an already-backfilled corpus is a no-op
(unless the exception list has changed).
"""

import os
import re
import sys
from pathlib import Path

BEINGS_DIR = Path(__file__).resolve().parent.parent / "data" / "beings"

# ── EXCEPTION LIST ──────────────────────────────────────────────────────
# Entries whose origin is NOT `manufactured`. Anything not listed here
# defaults to `manufactured`.

EXCEPTIONS = {
    # ── assembled (from parts of dead persons; new entity) ──────────
    "frankenstein-creature": "assembled",
    "universal-frankenstein-1931": "assembled",
    "young-frankenstein-creature": "assembled",
    "bride-of-frankenstein": "assembled",
    "creature-nick-dear-frankenstein": "assembled",
    "frankenstein-jr": "assembled",
    "herman-munster": "assembled",
    "shrike-mortal-engines": "assembled",

    # ── cloned (genetic/biological copy of a specific template) ─────
    "cleons-foundation-tv": "cloned",
    "jenny-doctors-daughter": "cloned",
    "call-alien-resurrection": "cloned",
    "illyasviel-fate": "cloned",
    "mickey-17": "cloned",
    "sons-a-number": "cloned",

    # ── copied (mind/pattern copied to new substrate; copy is own
    # narrative entity, distinct from the original) ─────────────────
    "cookie-white-christmas": "copied",
    "ashley-too-black-mirror": "copied",
    "bernard-westworld": "copied",
    "marjorie-prime-film": "copied",
    "walter-marjorie-prime-play": "copied",
    "white-vision-wandavision": "copied",
    "j-archive-2020": "copied",
    "daly-crew-uss-callister": "copied",
    "ash-be-right-back": "copied",
    "cherry-artifice-girl": "copied",

    # ── converted (living person biotechnically modified; result is
    # treated by the source text as a new being, not a continuation
    # of the prior person) ─────────────────────────────────────────
    "cybermen-doctor-who": "converted",
    "borg-collective": "converted",
    "locutus-borg": "converted",
    "seven-of-nine": "converted",
    "hugh-borg-tng": "converted",
    "borg-queen": "converted",
    "robocop-1987": "converted",
    "cain-robocop-2": "converted",
    "steve-austin-six-million": "converted",
    "jaime-sommers-bionic-woman": "converted",
    "modok-marvel": "converted",
    "deathlok-marvel": "converted",
    "robotman-doom-patrol": "converted",
    "cyborg-dc": "converted",
    "omac-dc": "converted",
    "davros-doctor-who": "converted",
    "airiam-discovery": "converted",
    "franky-one-piece": "converted",

    # ── transferred (mind moved from dying original to new substrate;
    # original ends, new being is presented as new) ────────────────
    "8-man-tobor": "transferred",
    "cyborg-superman": "transferred",
}


def determine_origin(entry_id: str) -> str:
    return EXCEPTIONS.get(entry_id, "manufactured")


SUBSTRATE_BLOCK_RE = re.compile(
    r"(^  substrate:\n(?:    - [^\n]+\n)+)",
    re.MULTILINE,
)

ORIGIN_LINE_RE = re.compile(r"^  origin: [a-z]+\n", re.MULTILINE)


def backfill_file(path: Path) -> tuple[bool, str]:
    """
    Backfill a single YAML file. Returns (changed, new_origin).

    Handles three cases:
      1. File has no `origin` line: insert one after `substrate:` block.
      2. File has an `origin` line with a different value: update it.
      3. File has the correct `origin` line: no-op.
    """
    entry_id = path.stem
    target_origin = determine_origin(entry_id)

    text = path.read_text(encoding="utf-8")
    desired_line = f"  origin: {target_origin}\n"

    existing = ORIGIN_LINE_RE.search(text)
    if existing:
        if existing.group(0) == desired_line:
            return False, target_origin
        new_text = text[: existing.start()] + desired_line + text[existing.end() :]
        path.write_text(new_text, encoding="utf-8")
        return True, target_origin

    # No origin line yet — insert after substrate block.
    m = SUBSTRATE_BLOCK_RE.search(text)
    if not m:
        raise RuntimeError(
            f"{path.name}: could not locate a `substrate:` block to insert "
            "the `origin:` line after."
        )

    insertion_point = m.end()
    new_text = text[:insertion_point] + desired_line + text[insertion_point:]
    path.write_text(new_text, encoding="utf-8")
    return True, target_origin


def main():
    files = sorted(BEINGS_DIR.glob("*.yaml"))
    if not files:
        print(f"No YAML files in {BEINGS_DIR}", file=sys.stderr)
        sys.exit(1)

    changed_count = 0
    unchanged_count = 0
    by_origin: dict[str, int] = {}

    for path in files:
        try:
            changed, origin_val = backfill_file(path)
        except Exception as exc:
            print(f"FAIL  {path.name}: {exc}", file=sys.stderr)
            sys.exit(1)
        by_origin[origin_val] = by_origin.get(origin_val, 0) + 1
        if changed:
            changed_count += 1
        else:
            unchanged_count += 1

    print(f"Processed {len(files)} files")
    print(f"  Changed:   {changed_count}")
    print(f"  Unchanged: {unchanged_count}")
    print("Origin distribution:")
    for k in sorted(by_origin):
        print(f"  {k:14s} {by_origin[k]:>4d}")


if __name__ == "__main__":
    main()
