# Boundary Cases

This directory is reserved for entries that sit on the edge of the schema — beings whose coding raises a problem the schema doesn't cleanly handle, and where the problem is interesting enough to document separately from the main corpus in `data/beings/`.

## What counts as a boundary case

An entry belongs here if **at least one** of the following is true:

1. **A required enum value doesn't quite fit.** The nearest option is clearly closer than the others, but the fit is bad enough that a future coder should know about it.
2. **The entry is not a constructed being in the strict sense**, but is included to make an exclusion decision explicit and defensible.
3. **The scope rules give an ambiguous answer.** For example: a transmedia character whose canonical "source text" is unclear, or a being who genuinely predates the scope rule (folklore, pre-print traditions).

An entry does **not** belong here merely because the coding was hard. Hard coding calls go in the `notes` field of the regular entry. Boundary cases are about structural mismatch between the schema and the being, not about analytical difficulty.

## Format

Boundary-case files follow the same schema as regular entries. Put the rationale for the boundary designation in `notes`, opened with a `BOUNDARY CASE:` marker so it's easy to find.

## Adding a boundary case

1. Copy `schema/entry_template.yaml` into `data/boundary_cases/`.
2. Code the fields as best you can — use the closest available enum value and explain the mismatch in `notes`.
3. Validate with `python schema/validate.py data/boundary_cases/your-file.yaml`.
4. Open a PR explaining why this entry belongs here rather than in `data/beings/`.
