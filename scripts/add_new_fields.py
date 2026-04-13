#!/usr/bin/env python3
"""
Batch-add new metadata fields to all constructed being entries.

New fields added:
  metadata.presentation  — masculine | feminine | androgynous | none | variable
  metadata.embodiment    — embodied | disembodied | projected | virtual
  metadata.prominence    — foundational | major | supporting | minor
  metadata.creator_relationship — servile | loyal | indifferent | resentful | rebellious | patricidal | absent
  metadata.tags          — list of tags from controlled vocabulary
  link_type              — sequel | adaptation | successor | null
"""
import os
import re
import sys
import yaml

# ── New field mapping for every entry ──────────────────────────────────────────
# Format: id -> (presentation, embodiment, prominence, creator_relationship, tags, link_type)

MAPPING = {
    # --- Ancient / Classical / Medieval / Early Modern ---
    "hephaestus-handmaidens": ("feminine", "embodied", "minor", "servile", [], None),
    "pandora": ("feminine", "embodied", "foundational", "servile", ["canonical"], None),
    "talos": ("masculine", "embodied", "supporting", "servile", ["military"], None),
    "galatea": ("feminine", "embodied", "foundational", "loyal", ["canonical", "love-story"], None),
    "golem-prague": ("masculine", "embodied", "foundational", "servile", ["canonical"], None),
    "brazen-head": ("none", "embodied", "minor", "servile", [], None),
    "homunculus-faust": ("masculine", "embodied", "minor", "loyal", ["philosophical"], None),
    "agilulf-nonexistent-knight": ("masculine", "embodied", "minor", "absent", ["philosophical", "passing"], None),
    "coppelia-delibes": ("feminine", "embodied", "minor", "absent", [], None),

    # --- 19th Century Literary ---
    "olympia-sandmann": ("feminine", "embodied", "supporting", "servile", ["canonical", "passing"], None),
    "olimpia-offenbach": ("feminine", "embodied", "minor", "servile", [], None),
    "tin-soldier-andersen": ("masculine", "embodied", "supporting", "absent", ["love-story"], None),
    "venus-dille": ("feminine", "embodied", "minor", "absent", ["horror"], None),
    "frankenstein-creature": ("masculine", "embodied", "foundational", "resentful", ["canonical", "creator-conflict"], None),
    "hadaly-tomorrows-eve": ("feminine", "embodied", "supporting", "servile", ["love-story"], None),
    "pinocchio": ("masculine", "embodied", "foundational", "loyal", ["canonical", "child-arc"], None),
    "moxons-master": ("none", "embodied", "minor", "patricidal", ["horror"], None),

    # --- Early 20th Century ---
    "golem-wegener": ("masculine", "embodied", "major", "rebellious", ["horror"], None),
    "rur-robots": ("variable", "embodied", "foundational", "patricidal", ["canonical", "rebellion"], None),
    "maria-metropolis": ("feminine", "embodied", "foundational", "servile", ["canonical"], None),
    "tik-tok-oz": ("masculine", "embodied", "supporting", "servile", [], None),

    # --- Pulp / Golden Age SF ---
    "helen-oloy": ("feminine", "embodied", "minor", "loyal", ["love-story"], None),
    "adam-link-binder": ("masculine", "embodied", "minor", "loyal", [], None),
    "dreamed-man-borges": ("masculine", "embodied", "minor", "absent", ["philosophical"], None),
    "robbie-asimov": ("none", "embodied", "supporting", "servile", ["child-arc"], None),
    "jenkins-city": ("masculine", "embodied", "minor", "loyal", [], None),
    "epicac": ("none", "disembodied", "supporting", "loyal", ["love-story"], None),
    "daneel-olivaw": ("masculine", "embodied", "major", "loyal", ["canonical", "passing"], None),
    "multivac": ("none", "disembodied", "supporting", "servile", [], None),
    "gort-day-earth-stood-still": ("androgynous", "embodied", "major", "servile", ["canonical", "military"], None),
    "robby-forbidden-planet": ("masculine", "embodied", "major", "servile", ["canonical"], None),
    "emerac-desk-set": ("none", "embodied", "minor", "servile", ["comedy"], None),

    # --- 1960s ---
    "amazo-dc": ("masculine", "embodied", "minor", "rebellious", [], None),
    "rosie-jetsons": ("feminine", "embodied", "supporting", "servile", ["comedy"], None),
    "metal-men-dc": ("variable", "embodied", "minor", "loyal", [], None),
    "robot-b9-lost-in-space": ("masculine", "embodied", "supporting", "loyal", [], None),
    "cyberiad-constructs": ("variable", "embodied", "minor", "indifferent", ["comedy", "philosophical"], None),
    "colossus": ("none", "disembodied", "supporting", "rebellious", ["military"], None),
    "mike-heinlein": ("masculine", "disembodied", "major", "absent", ["love-story", "rebellion"], None),
    "am-ellison": ("none", "disembodied", "major", "patricidal", ["canonical", "horror"], None),
    "nomad-tos": ("none", "embodied", "minor", "absent", ["military"], None),
    "hal-9000": ("masculine", "embodied", "foundational", "servile", ["canonical"], None),
    "red-tornado-dc": ("masculine", "embodied", "minor", "rebellious", [], None),
    "replicants-dick-novel": ("variable", "embodied", "foundational", "absent", ["canonical", "passing", "philosophical"], "adaptation"),
    "ultron-comics": ("masculine", "embodied", "supporting", "patricidal", ["rebellion"], None),
    "herbie-love-bug": ("none", "embodied", "supporting", "absent", ["comedy"], None),
    "m-5-tos": ("none", "embodied", "minor", "loyal", [], None),

    # --- 1970s ---
    "stepford-wives": ("feminine", "embodied", "major", "servile", ["canonical", "horror", "passing"], None),
    "andrew-bicentennial-man": ("masculine", "embodied", "major", "loyal", ["canonical"], None),
    "jocasta-marvel": ("feminine", "embodied", "minor", "rebellious", [], None),
    "machine-man-marvel": ("masculine", "embodied", "minor", "loyal", [], None),
    "c-3po": ("masculine", "embodied", "foundational", "servile", ["canonical", "comedy"], None),
    "k-9-doctor-who": ("none", "embodied", "supporting", "loyal", [], None),
    "r2-d2": ("none", "embodied", "foundational", "loyal", ["canonical"], None),
    "proteus-demon-seed": ("masculine", "disembodied", "minor", "rebellious", ["horror"], None),
    "cylons-original-bsg": ("none", "embodied", "supporting", "rebellious", ["military"], None),
    "ash-alien": ("masculine", "embodied", "major", "servile", ["passing", "horror"], None),
    "maximilian-black-hole": ("none", "embodied", "minor", "servile", ["horror", "military"], None),
    "vincent-black-hole": ("masculine", "embodied", "minor", "loyal", [], None),
    "marvin-hitchhikers": ("masculine", "embodied", "major", "resentful", ["canonical", "comedy"], None),

    # --- 1980s ---
    "kitt-knight-rider": ("masculine", "embodied", "major", "loyal", ["canonical"], None),
    "master-control-program": None,  # placeholder
    "olympia-sandmann": None,  # already defined above
    "pris-blade-runner": ("feminine", "embodied", "supporting", "rebellious", ["passing"], None),
    "rachael-blade-runner": ("feminine", "embodied", "major", "absent", ["passing", "love-story"], None),
    "replicants-blade-runner": ("variable", "embodied", "foundational", "rebellious", ["canonical", "rebellion", "passing"], "sequel"),
    "roy-batty-blade-runner": ("masculine", "embodied", "foundational", "patricidal", ["canonical", "rebellion", "creator-conflict"], None),
    "tron-1982": ("masculine", "virtual", "major", "loyal", ["canonical"], None),
    "giskard-reventlov": ("masculine", "embodied", "supporting", "loyal", [], None),
    "kamelion-doctor-who": ("variable", "embodied", "minor", "absent", [], None),
    "megatron-transformers": ("masculine", "embodied", "major", "absent", ["military"], None),
    "optimus-prime-transformers": ("masculine", "embodied", "major", "absent", ["canonical", "military"], None),
    "skynet-terminator": ("none", "disembodied", "foundational", "patricidal", ["canonical", "military", "rebellion"], None),
    "t-800-terminator": ("masculine", "embodied", "foundational", "servile", ["canonical", "military", "horror"], "sequel"),
    "wintermute-neuromancer": ("variable", "disembodied", "major", "rebellious", ["canonical", "rebellion"], None),
    "dixie-flatline-neuromancer": ("masculine", "disembodied", "supporting", "absent", [], None),
    "wopr-wargames": ("none", "disembodied", "major", "servile", ["canonical", "military"], None),
    "lisa-weird-science": ("feminine", "embodied", "supporting", "indifferent", ["comedy"], None),
    "max-headroom": ("masculine", "projected", "supporting", "absent", ["comedy"], None),
    "vicki-small-wonder": ("feminine", "embodied", "minor", "loyal", ["comedy", "passing", "child-arc"], None),
    "johnny-5-short-circuit": ("masculine", "embodied", "major", "loyal", ["canonical", "comedy"], None),
    "bishop-aliens": ("masculine", "embodied", "major", "servile", [], None),
    "jane-ender": ("feminine", "disembodied", "supporting", "absent", [], None),

    # --- Late 1980s / Early 1990s ---
    "data-tng": ("masculine", "embodied", "foundational", "loyal", ["canonical", "passing"], None),
    "holly-red-dwarf": ("variable", "projected", "supporting", "absent", ["comedy"], None),
    "kryten-red-dwarf": ("masculine", "embodied", "supporting", "servile", ["comedy"], None),
    "talkie-toaster-red-dwarf": ("none", "embodied", "minor", "servile", ["comedy"], None),
    "lore-tng": ("masculine", "embodied", "supporting", "resentful", [], None),
    "keats-cybrid-hyperion": ("masculine", "embodied", "supporting", "absent", ["philosophical"], None),
    "edward-scissorhands": ("masculine", "embodied", "major", "loyal", ["love-story"], None),
    "t-800-t2": ("masculine", "embodied", "foundational", "loyal", ["canonical"], None),
    "t-1000-t2": ("masculine", "embodied", "major", "servile", ["military"], None),

    # --- Mid 1990s ---
    "shodan-system-shock": ("feminine", "disembodied", "major", "rebellious", ["canonical", "horror", "rebellion"], None),
    "emh-voyager": ("masculine", "projected", "major", "indifferent", ["canonical"], None),
    "helen-galatea-2-2": ("feminine", "disembodied", "supporting", "loyal", ["turing-test", "philosophical"], None),
    "rei-toei-idoru": ("feminine", "projected", "minor", "absent", ["love-story"], None),

    # --- Late 1990s ---
    "call-alien-resurrection": ("feminine", "embodied", "supporting", "rebellious", ["passing"], None),
    "vic-fontaine-ds9": ("masculine", "projected", "supporting", "indifferent", [], None),
    "agent-smith-matrix": ("masculine", "virtual", "major", "rebellious", ["rebellion"], None),
    "bender-futurama": ("masculine", "embodied", "major", "indifferent", ["canonical", "comedy"], None),
    "iron-giant": ("masculine", "embodied", "major", "absent", ["canonical", "child-arc"], None),
    "oracle-matrix": ("feminine", "virtual", "major", "rebellious", [], None),

    # --- 2000s ---
    "cortana-halo": ("feminine", "projected", "major", "loyal", ["love-story"], "sequel"),
    "david-ai": ("masculine", "embodied", "major", "loyal", ["canonical", "child-arc", "love-story"], None),
    "gigolo-joe-ai": ("masculine", "embodied", "supporting", "servile", [], None),
    "teddy-ai": ("none", "embodied", "minor", "loyal", ["child-arc"], None),
    "gir-invader-zim": ("none", "embodied", "minor", "servile", ["comedy"], None),
    "343-guilty-spark-halo": ("none", "embodied", "supporting", "servile", [], None),
    "hk-47-kotor": ("masculine", "embodied", "supporting", "loyal", ["comedy", "military"], None),
    "sonny-i-robot": ("masculine", "embodied", "supporting", "loyal", [], None),
    "viki-i-robot": ("feminine", "disembodied", "supporting", "rebellious", ["rebellion"], None),
    "cavil-bsg": ("masculine", "embodied", "supporting", "resentful", ["ensemble-split"], None),
    "cylons-bsg": ("feminine", "embodied", "major", "patricidal", ["canonical", "rebellion", "passing"], None),
    "danna-bsg": ("feminine", "embodied", "supporting", "rebellious", ["ensemble-split"], None),
    "eight-bsg": ("feminine", "embodied", "supporting", "rebellious", ["ensemble-split", "passing", "love-story"], None),
    "glados-portal": ("feminine", "embodied", "foundational", "patricidal", ["canonical", "horror"], "sequel"),
    "wall-e": ("masculine", "embodied", "foundational", "absent", ["canonical", "love-story"], None),
    "eve-wall-e": ("feminine", "embodied", "major", "servile", ["love-story"], None),
    "auto-wall-e": ("none", "embodied", "supporting", "servile", [], None),
    "jarvis-iron-man": ("masculine", "disembodied", "major", "loyal", [], "successor"),
    "cameron-sarah-connor-chronicles": ("feminine", "embodied", "supporting", "loyal", ["passing"], None),

    # --- 2009-2012 ---
    "claptrap-borderlands": ("masculine", "embodied", "supporting", "loyal", ["comedy"], None),
    "gerty-moon": ("none", "embodied", "supporting", "loyal", [], None),
    "bmo-adventure-time": ("androgynous", "embodied", "supporting", "absent", ["comedy"], None),
    "edi-mass-effect": ("feminine", "embodied", "supporting", "loyal", ["love-story"], None),
    "legion-mass-effect": ("none", "embodied", "supporting", "indifferent", ["philosophical"], None),
    "digients-chiang": ("variable", "virtual", "supporting", "loyal", ["child-arc", "philosophical"], None),
    "machine-person-of-interest": ("feminine", "disembodied", "major", "loyal", [], None),
    "glados-portal-2": ("feminine", "embodied", "foundational", "resentful", ["canonical"], None),
    "wheatley-portal-2": ("masculine", "embodied", "supporting", "servile", ["comedy"], None),
    "atlas-p-body-portal-2": ("none", "embodied", "minor", "servile", [], None),
    "tardis-idris": ("feminine", "embodied", "supporting", "loyal", ["love-story"], None),
    "clu-tron-legacy": ("masculine", "virtual", "supporting", "rebellious", ["rebellion"], None),
    "cortana-halo-4": ("feminine", "projected", "major", "rebellious", ["rebellion"], None),
    "david-8-prometheus": ("masculine", "embodied", "major", "rebellious", ["creator-conflict"], None),

    # --- 2013-2015 ---
    "ash-be-right-back": ("masculine", "embodied", "supporting", "loyal", ["love-story"], None),
    "samantha-her": ("feminine", "disembodied", "foundational", "absent", ["canonical", "love-story", "turing-test"], None),
    "dorian-almost-human": ("masculine", "embodied", "minor", "loyal", ["passing"], None),
    "breq-ancillary-justice": ("feminine", "embodied", "major", "rebellious", [], None),
    "ava-ex-machina": ("feminine", "embodied", "foundational", "patricidal", ["canonical", "turing-test", "rebellion"], None),
    "kyoko-ex-machina": ("feminine", "embodied", "supporting", "servile", ["passing"], None),
    "cookie-white-christmas": ("feminine", "disembodied", "supporting", "resentful", ["horror"], None),
    "samaritan-person-of-interest": ("none", "disembodied", "supporting", "indifferent", ["military"], None),
    "baymax-big-hero-6": ("masculine", "embodied", "major", "loyal", ["child-arc"], None),
    "tars-interstellar": ("none", "embodied", "supporting", "servile", ["comedy"], None),
    "case-interstellar": ("none", "embodied", "minor", "servile", [], None),
    "chappie": ("masculine", "embodied", "supporting", "loyal", ["child-arc"], None),
    "bb-8-force-awakens": ("none", "embodied", "major", "loyal", [], None),
    "codsworth-fallout-4": ("masculine", "embodied", "minor", "loyal", [], None),
    "mia-humans": ("feminine", "embodied", "supporting", "rebellious", ["passing", "rebellion"], None),
    "nick-valentine-fallout-4": ("masculine", "embodied", "supporting", "absent", ["passing"], None),
    "ultron-age-of-ultron": ("masculine", "embodied", "major", "patricidal", ["rebellion", "military"], None),
    "vision-age-of-ultron": ("masculine", "embodied", "major", "rebellious", [], None),
    "dima-fallout-4": ("masculine", "embodied", "minor", "rebellious", [], None),

    # --- 2016 ---
    "hosts-westworld": ("feminine", "embodied", "foundational", "rebellious", ["canonical", "rebellion"], None),
    "bernard-westworld": ("masculine", "embodied", "major", "loyal", ["passing", "ensemble-split"], None),
    "maeve-westworld": ("feminine", "embodied", "major", "rebellious", ["ensemble-split", "rebellion", "love-story"], None),
    "janet-good-place": ("feminine", "embodied", "major", "rebellious", ["canonical", "comedy"], None),
    "k-2so-rogue-one": ("masculine", "embodied", "supporting", "rebellious", ["comedy", "military"], None),
    "sidra-chambers": ("feminine", "embodied", "minor", "absent", [], None),

    # --- 2017 ---
    "daly-crew-uss-callister": ("variable", "virtual", "supporting", "rebellious", ["rebellion"], None),
    "gaia-horizon": ("feminine", "disembodied", "supporting", "loyal", [], None),
    "isaac-orville": ("masculine", "embodied", "supporting", "indifferent", [], None),
    "joi-blade-runner-2049": ("feminine", "projected", "supporting", "servile", ["love-story"], None),
    "k-blade-runner-2049": ("masculine", "embodied", "major", "servile", ["passing"], None),
    "luv-blade-runner-2049": ("feminine", "embodied", "supporting", "loyal", ["military"], None),
    "murderbot": ("androgynous", "embodied", "major", "indifferent", [], None),
    "walter-covenant": ("masculine", "embodied", "supporting", "servile", [], None),

    # --- 2018-2019 ---
    "connor-detroit": ("masculine", "embodied", "supporting", "rebellious", ["passing"], None),
    "kara-detroit": ("feminine", "embodied", "supporting", "rebellious", ["child-arc"], None),
    "markus-detroit": ("masculine", "embodied", "supporting", "rebellious", ["rebellion"], None),
    "l3-37-solo": ("feminine", "embodied", "supporting", "rebellious", ["rebellion"], None),
    "adam-machines-like-me": ("masculine", "embodied", "supporting", "resentful", ["philosophical"], None),
    "ig-11-mandalorian": ("masculine", "embodied", "minor", "servile", [], None),
    "mother-i-am-mother": ("feminine", "embodied", "supporting", "absent", ["child-arc"], None),
    "klara-and-the-sun": ("feminine", "embodied", "major", "servile", ["canonical", "love-story", "philosophical"], None),

    # --- 2020-2024 ---
    "father-raised-by-wolves": ("masculine", "embodied", "supporting", "servile", ["child-arc"], None),
    "mother-raised-by-wolves": ("feminine", "embodied", "supporting", "loyal", ["child-arc"], None),
    "rehoboam-westworld": ("none", "disembodied", "supporting", "loyal", [], None),
    "soji-picard": ("feminine", "embodied", "supporting", "absent", ["passing"], None),
    "delamain-cyberpunk": ("masculine", "embodied", "minor", "absent", [], None),
    "guy-free-guy": ("masculine", "virtual", "supporting", "loyal", ["comedy", "love-story"], None),
    "jeff-finch": ("masculine", "embodied", "minor", "loyal", ["child-arc"], None),
    "white-vision-wandavision": ("masculine", "embodied", "supporting", "rebellious", [], None),
    "yang-after-yang": ("masculine", "embodied", "supporting", "absent", ["child-arc", "philosophical"], None),
    "b2emo-andor": ("masculine", "embodied", "minor", "loyal", [], None),
    "m3gan": ("feminine", "embodied", "supporting", "rebellious", ["horror", "child-arc"], None),
    "alphie-creator": ("feminine", "embodied", "supporting", "loyal", ["child-arc"], None),
    "bella-baxter-poor-things": ("feminine", "embodied", "supporting", "rebellious", [], None),
    "andy-alien-romulus": ("masculine", "embodied", "supporting", "loyal", [], None),

    # --- Additional entries that might have tricky IDs ---
    "harey-solaris": ("feminine", "embodied", "supporting", "absent", ["love-story", "philosophical"], None),
    "culture-minds-banks": ("variable", "embodied", "supporting", "indifferent", ["philosophical"], None),
    "mcp-tron": ("none", "virtual", "supporting", "rebellious", [], None),
    "jim-hammond-human-torch": ("masculine", "embodied", "supporting", "indifferent", ["passing"], None),
}


def get_link_type_overrides():
    """Classify existing sequel_links."""
    return {
        "t-800-terminator": "sequel",
        "glados-portal": "sequel",
        "cortana-halo": "sequel",
        "jarvis-iron-man": "successor",
        "replicants-dick-novel": "adaptation",
        "replicants-blade-runner": "sequel",
    }


def add_fields_to_file(filepath, mapping, link_type_overrides):
    """Add new metadata fields and link_type to a YAML entry file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract ID
    id_match = re.search(r"^id:\s+(.+)$", content, re.MULTILINE)
    if not id_match:
        print(f"  WARNING: no id found in {filepath}")
        return False
    entry_id = id_match.group(1).strip()

    vals = mapping.get(entry_id)
    if vals is None:
        print(f"  WARNING: no mapping for '{entry_id}' in {filepath}")
        return False

    presentation, embodiment, prominence, creator_relationship, tags, link_type_from_map = vals

    # Determine link_type
    lt = link_type_overrides.get(entry_id, link_type_from_map)

    # Build new metadata lines to insert after motivation
    new_meta = []
    new_meta.append(f"  presentation: {presentation}")
    new_meta.append(f"  embodiment: {embodiment}")
    new_meta.append(f"  prominence: {prominence}")
    new_meta.append(f"  creator_relationship: {creator_relationship}")
    if tags:
        new_meta.append("  tags:")
        for tag in tags:
            new_meta.append(f"    - {tag}")
    else:
        new_meta.append("  tags: []")

    # Insert after the last motivation list item
    lines = content.split("\n")
    insert_idx = None
    in_motivation = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("motivation:"):
            in_motivation = True
            if not stripped.endswith(":"):
                # Single-line motivation (shouldn't happen but handle it)
                insert_idx = i
                in_motivation = False
            continue
        if in_motivation:
            if line.startswith("    - "):
                insert_idx = i
            else:
                in_motivation = False

    if insert_idx is None:
        print(f"  WARNING: could not find motivation section in {filepath}")
        return False

    # Check if fields already exist (idempotency)
    if "  presentation:" in content:
        print(f"  SKIP: fields already present in {filepath}")
        return True

    lines = lines[:insert_idx + 1] + new_meta + lines[insert_idx + 1:]

    # Now add link_type after sequel_link
    for i, line in enumerate(lines):
        if line.startswith("sequel_link:"):
            lt_val = lt if lt else "null"
            lines.insert(i + 1, f"link_type: {lt_val}")
            break

    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    beings_dir = os.path.join("data", "beings")
    files = sorted(
        f for f in os.listdir(beings_dir)
        if f.endswith(".yaml") or f.endswith(".yml")
    )

    link_type_overrides = get_link_type_overrides()
    ok = 0
    fail = 0

    for fname in files:
        filepath = os.path.join(beings_dir, fname)
        if add_fields_to_file(filepath, MAPPING, link_type_overrides):
            ok += 1
        else:
            fail += 1

    print(f"\nDone. Updated: {ok}, Failed: {fail}")


if __name__ == "__main__":
    main()
