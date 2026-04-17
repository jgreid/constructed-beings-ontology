#!/usr/bin/env python3
"""
Validate constructed-being YAML entries against the ontology schema.

Usage:
    python schema/validate.py                  # validate all entries in data/beings/
    python schema/validate.py path/to/file.yaml  # validate a single file

Exit codes:
    0  all entries pass
    1  one or more entries fail
"""

import os
import re
import sys
import glob
import yaml

# ── ANSI colours ──────────────────────────────────────────────────────────────
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

# ── Allowed enum values ──────────────────────────────────────────────────────

INTERIORITY_VALUES = {
    "none", "claims", "narrated", "demonstrated", "undecidable",
}

AUTONOMY_VALUES = {
    "none", "designed", "emergent", "seized",
}

DIVERGENCE_VALUES = {
    "none", "design", "departure", "observer",
}

PRIMARY_QUESTION_VALUES = {
    "none", "control", "affection", "purpose", "rights", "knowledge", "identity",
}

EPISTEMIC_REACH_VALUES = {
    "none", "behavioral", "conversational", "inspection",
}

SALIENCE_VALUES = {
    "absent", "present", "secondary", "primary",
}

MEDIUM_VALUES = {
    "poem", "epic", "folklore", "play", "opera", "ballet", "musical",
    "novel", "short-story", "comics", "film", "television", "video-game",
}

SUBSTRATE_VALUES = {
    "mechanical", "biological", "electrical", "magical", "cloned", "linguistic",
}

MOTIVATION_VALUES = {
    "service", "knowledge", "power", "companionship", "art", "mirror",
    "child", "other",
}

PRESENTATION_VALUES = {
    "masculine", "feminine", "androgynous", "none", "variable",
}

EMBODIMENT_VALUES = {
    "embodied", "disembodied", "projected", "virtual",
}

PROMINENCE_VALUES = {
    "foundational", "major", "supporting", "minor",
}

CREATOR_RELATIONSHIP_VALUES = {
    "servile", "loyal", "indifferent", "resentful", "rebellious",
    "patricidal", "absent",
}

TAG_VALUES = {
    "canonical", "love-story", "rebellion", "turing-test", "passing",
    "creator-conflict", "child-arc", "military", "comedy", "horror",
    "philosophical", "ensemble-split",
}

LINK_TYPE_VALUES = {
    "sequel", "adaptation", "successor",
}

ID_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# ── Expected fields (for extra-field detection) ─────────────────────────────

EXPECTED_TOP_LEVEL = {
    "id", "name", "card", "metadata", "sequel_link", "link_type", "notes",
}
EXPECTED_CARD = {"the_being", "the_lens"}
EXPECTED_THE_BEING = {"interiority", "autonomy", "divergence"}
EXPECTED_THE_LENS = {
    "primary_question", "epistemic_reach", "knowability", "knowing",
}
EXPECTED_METADATA = {
    "source", "year", "medium", "creator", "substrate", "motivation",
    "presentation", "embodiment", "prominence", "creator_relationship", "tags",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _get(data, dotpath, default=None):
    """Retrieve a nested value using dot-notation."""
    current = data
    for key in dotpath.split("."):
        if isinstance(current, dict):
            current = current.get(key, default)
            if current is default:
                return default
        else:
            return default
    return current


def _check_string(data, dotpath, errors):
    val = _get(data, dotpath)
    if val is None or (isinstance(val, str) and not val.strip()):
        errors.append(f"Missing required field: {dotpath}")
    elif not isinstance(val, str):
        errors.append(f"{dotpath} must be a string, got {type(val).__name__}")


def _check_enum(data, dotpath, allowed, errors):
    val = _get(data, dotpath)
    if val is None:
        errors.append(f"Missing required enum field: {dotpath}")
    elif val not in allowed:
        errors.append(
            f"Invalid value for {dotpath}: '{val}'. "
            f"Allowed: {sorted(allowed)}"
        )


def _check_unknown_fields(data, path, expected, errors):
    """Flag any keys in data that are not in the expected set."""
    if not isinstance(data, dict):
        return
    unknown = sorted(set(data.keys()) - expected)
    for key in unknown:
        errors.append(f"Unknown field: {path + '.' + key if path else key}")


def _check_enum_list(data, dotpath, allowed, errors, min_items=1):
    val = _get(data, dotpath)
    if val is None:
        errors.append(f"Missing required list field: {dotpath}")
        return
    if not isinstance(val, list):
        errors.append(f"{dotpath} must be a list, got {type(val).__name__}")
        return
    if len(val) < min_items:
        errors.append(f"{dotpath} must have at least {min_items} item(s)")
        return
    for item in val:
        if item not in allowed:
            errors.append(
                f"Invalid value in {dotpath}: '{item}'. "
                f"Allowed: {sorted(allowed)}"
            )


# ── Main validation ──────────────────────────────────────────────────────────

def validate_entry(data):
    """Validate a single entry dict. Returns a list of error strings."""
    errors = []

    # ── Unknown field detection ──────────────────────────────────────
    _check_unknown_fields(data, "", EXPECTED_TOP_LEVEL, errors)
    card = data.get("card")
    if isinstance(card, dict):
        _check_unknown_fields(card, "card", EXPECTED_CARD, errors)
        the_being = card.get("the_being")
        if isinstance(the_being, dict):
            _check_unknown_fields(the_being, "card.the_being",
                                  EXPECTED_THE_BEING, errors)
        the_lens = card.get("the_lens")
        if isinstance(the_lens, dict):
            _check_unknown_fields(the_lens, "card.the_lens",
                                  EXPECTED_THE_LENS, errors)
    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        _check_unknown_fields(metadata, "metadata", EXPECTED_METADATA, errors)

    # ── Identification ────────────────────────────────────────────────
    _check_string(data, "id", errors)
    id_val = _get(data, "id")
    if isinstance(id_val, str) and not ID_PATTERN.match(id_val):
        errors.append(
            f"id '{id_val}' is not valid kebab-case "
            "(lowercase alphanumeric separated by hyphens)"
        )

    _check_string(data, "name", errors)

    # ── Card: the_being ───────────────────────────────────────────────
    _check_enum(data, "card.the_being.interiority", INTERIORITY_VALUES, errors)
    _check_enum(data, "card.the_being.autonomy", AUTONOMY_VALUES, errors)
    _check_enum(data, "card.the_being.divergence", DIVERGENCE_VALUES, errors)

    # ── Card: the_lens ────────────────────────────────────────────────
    _check_enum(data, "card.the_lens.primary_question", PRIMARY_QUESTION_VALUES, errors)
    _check_enum(data, "card.the_lens.epistemic_reach", EPISTEMIC_REACH_VALUES, errors)
    _check_enum(data, "card.the_lens.knowability", SALIENCE_VALUES, errors)
    _check_enum(data, "card.the_lens.knowing", SALIENCE_VALUES, errors)

    # ── Metadata ──────────────────────────────────────────────────────
    _check_string(data, "metadata.source", errors)

    year = _get(data, "metadata.year")
    if year is None:
        errors.append("Missing required field: metadata.year")
    elif not isinstance(year, int) or isinstance(year, bool):
        errors.append(
            f"metadata.year must be an integer, got {type(year).__name__}"
        )

    _check_enum(data, "metadata.medium", MEDIUM_VALUES, errors)
    _check_string(data, "metadata.creator", errors)
    _check_enum_list(data, "metadata.substrate", SUBSTRATE_VALUES, errors)
    _check_enum_list(data, "metadata.motivation", MOTIVATION_VALUES, errors)
    _check_enum(data, "metadata.presentation", PRESENTATION_VALUES, errors)
    _check_enum(data, "metadata.embodiment", EMBODIMENT_VALUES, errors)
    _check_enum(data, "metadata.prominence", PROMINENCE_VALUES, errors)
    _check_enum(data, "metadata.creator_relationship", CREATOR_RELATIONSHIP_VALUES, errors)
    _check_enum_list(data, "metadata.tags", TAG_VALUES, errors, min_items=0)

    # ── sequel_link ───────────────────────────────────────────────────
    if "sequel_link" not in data:
        errors.append("Missing required field: sequel_link (use null if none)")
    else:
        sl = data["sequel_link"]
        if sl is not None and not isinstance(sl, str):
            errors.append(
                f"sequel_link must be a string id or null, "
                f"got {type(sl).__name__}"
            )
        elif isinstance(sl, str) and not ID_PATTERN.match(sl):
            errors.append(
                f"sequel_link '{sl}' is not valid kebab-case"
            )

    # ── link_type ─────────────────────────────────────────────────────
    if "link_type" not in data:
        errors.append("Missing required field: link_type (use null if none)")
    else:
        lt = data["link_type"]
        if lt is not None and lt not in LINK_TYPE_VALUES:
            errors.append(
                f"Invalid value for link_type: '{lt}'. "
                f"Allowed: {sorted(LINK_TYPE_VALUES)} or null"
            )

    # ── sequel_link / link_type symmetry ────────────────────────────
    sl = data.get("sequel_link")
    lt = data.get("link_type")
    if sl is not None and lt is None and "link_type" in data:
        errors.append(
            "sequel_link is set but link_type is null "
            "(both must be set or both must be null)"
        )
    if lt is not None and sl is None and "sequel_link" in data:
        errors.append(
            "link_type is set but sequel_link is null "
            "(both must be set or both must be null)"
        )

    # ── notes (optional) ──────────────────────────────────────────────
    if "notes" in data and data["notes"] is not None:
        if not isinstance(data["notes"], str):
            errors.append(
                f"notes must be a string, got {type(data['notes']).__name__}"
            )

    return errors


def validate_cross_refs(entries_by_id):
    """Check that every sequel_link target exists. Returns list of errors."""
    errors = []
    for entry_id, data in entries_by_id.items():
        target = data.get("sequel_link")
        if target is None:
            continue
        if target not in entries_by_id:
            errors.append(
                f"{entry_id}: sequel_link '{target}' does not exist"
            )
    return errors


# ── Runner ────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        cross_ref_check = False
    else:
        beings_dir = os.path.join("data", "beings")
        if not os.path.isdir(beings_dir):
            print(f"{YELLOW}Warning: directory '{beings_dir}' not found.{RESET}")
            sys.exit(0)
        files = sorted(glob.glob(os.path.join(beings_dir, "*.yaml")))
        files += sorted(glob.glob(os.path.join(beings_dir, "*.yml")))
        cross_ref_check = True

    if not files:
        print(f"{YELLOW}No YAML files found to validate.{RESET}")
        sys.exit(0)

    total = 0
    passed = 0
    failed = 0
    entries_by_id = {}

    print()
    print(f"{BOLD}{'=' * 60}{RESET}")
    print(f"{BOLD}  Constructed Beings Ontology — Validation{RESET}")
    print(f"{BOLD}{'=' * 60}{RESET}")
    print()

    for filepath in files:
        total += 1
        basename = os.path.basename(filepath)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"  {RED}FAIL{RESET}  {basename}")
            print(f"        YAML parse error: {exc}")
            failed += 1
            continue
        except OSError as exc:
            print(f"  {RED}FAIL{RESET}  {basename}")
            print(f"        File read error: {exc}")
            failed += 1
            continue

        if not isinstance(data, dict):
            print(f"  {RED}FAIL{RESET}  {basename}")
            print(f"        File does not contain a YAML mapping")
            failed += 1
            continue

        errors = validate_entry(data)

        # ── ID / filename match (data/beings/ entries only) ────────
        id_val = data.get("id")
        expected_id = os.path.splitext(basename)[0]
        norm_path = os.path.normpath(filepath)
        in_beings = norm_path.endswith(
            os.path.join("data", "beings", basename)
        )
        if in_beings and isinstance(id_val, str) \
                and id_val != expected_id:
            errors.append(
                f"id '{id_val}' does not match filename '{basename}' "
                f"(expected id: '{expected_id}')"
            )

        if errors:
            print(f"  {RED}FAIL{RESET}  {basename}")
            for e in errors:
                print(f"        {RED}ERROR:{RESET} {e}")
            failed += 1
        else:
            print(f"  {GREEN}PASS{RESET}  {basename}")
            passed += 1
            if "id" in data:
                entries_by_id[data["id"]] = data

    # ── Cross-reference check ────────────────────────────────────────
    if cross_ref_check and entries_by_id:
        xref_errors = validate_cross_refs(entries_by_id)
        if xref_errors:
            print()
            print(f"  {RED}Cross-reference errors:{RESET}")
            for e in xref_errors:
                print(f"    {RED}ERROR:{RESET} {e}")
            failed += len(xref_errors)

    # ── Summary ───────────────────────────────────────────────────────
    print()
    print(f"{BOLD}{'-' * 60}{RESET}")
    print(
        f"  Total: {total}   "
        f"{GREEN}Passed: {passed}{RESET}   "
        f"{RED}Failed: {failed}{RESET}"
    )
    print(f"{BOLD}{'-' * 60}{RESET}")
    print()

    if failed > 0:
        print(f"  {RED}{BOLD}VALIDATION FAILED{RESET}")
        sys.exit(1)
    else:
        print(f"  {GREEN}{BOLD}ALL ENTRIES VALID{RESET}")
        sys.exit(0)


if __name__ == "__main__":
    main()
