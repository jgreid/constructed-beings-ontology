#!/usr/bin/env python3
"""
Validate constructed-being YAML entries against the ontology schema.

Usage:
    python schema/validate.py          # from repo root
    python schema/validate.py [path]   # validate a single file

Exit codes:
    0  all entries pass
    1  one or more entries fail
"""

import os
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

MEDIUM_VALUES = {
    "novel", "short-story", "play", "poem", "epic", "film",
    "television", "video-game", "myth", "folklore", "opera", "sacred-text",
}

REPRODUCTIVE_METHOD_VALUES = {
    "made", "born-sexual", "born-clonal", "born-parthenogenic",
    "born-divine", "ambiguous",
}

MOTIVATION_VALUES = {
    "M-SRV", "M-COM", "M-CHI", "M-KNO", "M-POW", "M-MIR", "M-ART", "M-OTH",
}

CREATION_MORALITY_VALUES = {
    "CM-MOR", "CM-IMM", "CM-AMO", "CM-AMB", "CM-RET",
}

SUBSTRATE_VALUES = {
    "S-BIO", "S-MEC", "S-ELE", "S-MAG", "S-HYB", "S-LIN", "S-CLO", "S-OTH",
}

AUTONOMY_VALUES = {
    "A-NON", "A-EMR", "A-DES", "A-SEI", "A-AMB",
}

INTERIORITY_VALUES = {
    "I-NON", "I-CLM", "I-NAR", "I-DEM", "I-DEN", "I-UND",
}

MORTALITY_VALUES = {
    "L-MOR", "L-IMM", "L-DES", "L-RES", "L-EPH", "L-UNK",
}

MULTIPLICITY_VALUES = {
    "MU-ONE", "MU-FEW", "MU-MAN", "MU-INF",
}

MEMORY_PERSISTENCE_VALUES = {
    "P-NON", "P-CON", "P-WIP", "P-SES", "P-SEL", "P-UNK",
}

NCT_VALUES = {
    "NCT-YES", "NCT-NO", "NCT-NA",
}

FAILURE_MODE_VALUES = {
    "F-EXC", "F-REV", "F-DEM", "F-AUT", "F-IND", "F-MUT", "F-NON", "F-OTH",
}

QUESTION_VALUES = {
    "Q-OBY", "Q-CTL", "Q-FEL", "Q-LOV", "Q-TEL", "Q-RTS", "Q-KNO", "Q-OTH",
}

EPISTEMIC_REACH_VALUES = {
    "ER-NON", "ER-DAT", "ER-BEH", "ER-PER", "ER-CON", "ER-UNK",
}

QK_STATUS_VALUES = {
    "QK-ABS", "QK-INFRA", "QK-SEC", "QK-PRI",
}

NARRATIVE_ROLE_VALUES = {
    "NR-SUB", "NR-MAJ", "NR-MIN", "NR-BKG",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _get(data, dotpath, default=None):
    """Retrieve a nested value using dot-notation."""
    keys = dotpath.split(".")
    current = data
    for k in keys:
        if isinstance(current, dict):
            current = current.get(k, default)
        else:
            return default
    return current


def _check_required_scalar(data, dotpath, errors, label=None):
    """Ensure a required scalar field is present and non-empty."""
    label = label or dotpath
    val = _get(data, dotpath)
    if val is None or (isinstance(val, str) and val.strip() == ""):
        errors.append(f"Missing required field: {label}")


def _check_enum(data, dotpath, allowed, errors, label=None):
    """Ensure a scalar field is one of the allowed enum values."""
    label = label or dotpath
    val = _get(data, dotpath)
    if val is None:
        errors.append(f"Missing required enum field: {label}")
    elif val not in allowed:
        errors.append(
            f"Invalid value for {label}: '{val}'. "
            f"Allowed: {sorted(allowed)}"
        )


def _check_enum_list(data, dotpath, allowed, errors, label=None, min_items=1):
    """Ensure a list field contains only allowed enum values."""
    label = label or dotpath
    val = _get(data, dotpath)
    if val is None:
        errors.append(f"Missing required list field: {label}")
        return
    if not isinstance(val, list):
        errors.append(f"{label} must be a list, got {type(val).__name__}")
        return
    if len(val) < min_items:
        errors.append(f"{label} must have at least {min_items} item(s)")
        return
    for item in val:
        if item not in allowed:
            errors.append(
                f"Invalid value in {label}: '{item}'. "
                f"Allowed: {sorted(allowed)}"
            )


def _check_optional_warn(data, dotpath, warnings, label=None):
    """Warn (don't error) if an optional field is missing."""
    label = label or dotpath
    val = _get(data, dotpath)
    if val is None:
        warnings.append(f"Optional field missing: {label}")


# ── Main validation ──────────────────────────────────────────────────────────

def validate_entry(data, filename):
    """Validate a single entry dict. Returns (errors, warnings)."""
    errors = []
    warnings = []

    # ── Identification ────────────────────────────────────────────────
    _check_required_scalar(data, "id", errors)
    id_val = _get(data, "id")
    if id_val and not isinstance(id_val, str):
        errors.append(f"id must be a string, got {type(id_val).__name__}")
    elif id_val and id_val != id_val.lower().replace(" ", "-"):
        # loose kebab-case check
        import re
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', id_val):
            errors.append(
                f"id '{id_val}' is not valid kebab-case "
                "(lowercase alphanumeric separated by hyphens)"
            )

    _check_required_scalar(data, "name", errors)
    _check_optional_warn(data, "aliases", warnings)

    # ── Source ────────────────────────────────────────────────────────
    _check_required_scalar(data, "source.author", errors)
    _check_required_scalar(data, "source.title", errors)

    year = _get(data, "source.year")
    if year is None:
        errors.append("Missing required field: source.year")
    elif not isinstance(year, int):
        errors.append(f"source.year must be an integer, got {type(year).__name__}")

    _check_enum(data, "source.medium", MEDIUM_VALUES, errors)
    _check_required_scalar(data, "source.tradition", errors)

    # ── Reproductive method ───────────────────────────────────────────
    _check_enum(data, "reproductive_method", REPRODUCTIVE_METHOD_VALUES, errors)
    rm = _get(data, "reproductive_method")
    if rm and isinstance(rm, str) and rm.startswith("born-"):
        errors.append(
            f"reproductive_method '{rm}' is a born-* value. "
            "Only 'made' or 'ambiguous' are accepted for constructed beings. "
            "If this being was born rather than made, it may not belong in "
            "this ontology."
        )

    # ── Creator ───────────────────────────────────────────────────────
    _check_required_scalar(data, "creator.name", errors)
    _check_enum_list(data, "creator.motivation", MOTIVATION_VALUES, errors)
    _check_enum(data, "creator.creation_morality", CREATION_MORALITY_VALUES, errors)

    # ── Being ─────────────────────────────────────────────────────────
    _check_enum_list(data, "being.substrate", SUBSTRATE_VALUES, errors)
    _check_enum(data, "being.autonomy", AUTONOMY_VALUES, errors)
    _check_optional_warn(data, "being.autonomy_trajectory", warnings)
    _check_enum(data, "being.interiority", INTERIORITY_VALUES, errors)
    _check_enum(data, "being.mortality", MORTALITY_VALUES, errors)
    _check_enum(data, "being.multiplicity", MULTIPLICITY_VALUES, errors)
    _check_enum(data, "being.memory_persistence", MEMORY_PERSISTENCE_VALUES, errors)
    _check_enum(data, "being.nonconsensual_transformation", NCT_VALUES, errors)

    # ── Relationship ──────────────────────────────────────────────────
    _check_enum_list(data, "relationship.failure_mode", FAILURE_MODE_VALUES, errors)
    _check_enum_list(data, "relationship.question", QUESTION_VALUES, errors)
    _check_enum(data, "relationship.question_primary", QUESTION_VALUES, errors)
    _check_enum(data, "relationship.epistemic_reach", EPISTEMIC_REACH_VALUES, errors)
    _check_enum(data, "relationship.q_kno_status", QK_STATUS_VALUES, errors)

    # ── Citations ─────────────────────────────────────────────────────
    citations = _get(data, "citations")
    if citations is None:
        errors.append("Missing required field: citations")
    elif not isinstance(citations, list):
        errors.append(f"citations must be a list, got {type(citations).__name__}")
    elif len(citations) < 1:
        errors.append("At least one citation is required")
    else:
        for i, cit in enumerate(citations):
            prefix = f"citations[{i}]"
            if not isinstance(cit, dict):
                errors.append(f"{prefix} must be a mapping")
                continue
            for req in ("property", "text", "location"):
                if req not in cit or not cit[req]:
                    errors.append(f"Missing required field: {prefix}.{req}")
            if "note" not in cit:
                warnings.append(f"Optional field missing: {prefix}.note")

    # ── Notes (optional) ──────────────────────────────────────────────
    _check_optional_warn(data, "notes", warnings)

    # ── Narrative role ────────────────────────────────────────────────
    _check_enum(data, "narrative_role", NARRATIVE_ROLE_VALUES, errors)

    return errors, warnings


# ── Runner ────────────────────────────────────────────────────────────────────

def main():
    # Determine files to validate
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        beings_dir = os.path.join("data", "beings")
        if not os.path.isdir(beings_dir):
            print(f"{YELLOW}Warning: directory '{beings_dir}' not found.{RESET}")
            print(f"{YELLOW}No entries to validate.{RESET}")
            sys.exit(0)
        files = sorted(glob.glob(os.path.join(beings_dir, "*.yaml")))
        files += sorted(glob.glob(os.path.join(beings_dir, "*.yml")))

    if not files:
        print(f"{YELLOW}No YAML files found to validate.{RESET}")
        sys.exit(0)

    total = 0
    passed = 0
    failed = 0
    warned = 0

    print()
    print(f"{BOLD}{'=' * 60}{RESET}")
    print(f"{BOLD}  Constructed Beings Ontology — Validation Report{RESET}")
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

        errors, warnings = validate_entry(data, basename)

        if errors:
            print(f"  {RED}FAIL{RESET}  {basename}")
            for e in errors:
                print(f"        {RED}ERROR:{RESET} {e}")
            for w in warnings:
                print(f"        {YELLOW}WARN:{RESET}  {w}")
            failed += 1
        elif warnings:
            print(f"  {GREEN}PASS{RESET}  {basename}")
            for w in warnings:
                print(f"        {YELLOW}WARN:{RESET}  {w}")
            passed += 1
            warned += 1
        else:
            print(f"  {GREEN}PASS{RESET}  {basename}")
            passed += 1

    # ── Summary ───────────────────────────────────────────────────────
    print()
    print(f"{BOLD}{'-' * 60}{RESET}")
    print(
        f"  Total: {total}   "
        f"{GREEN}Passed: {passed}{RESET}   "
        f"{RED}Failed: {failed}{RESET}   "
        f"{YELLOW}Warnings: {warned}{RESET}"
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
