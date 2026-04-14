## Summary

<!-- What does this PR do? New entry, correction, schema change, documentation, tooling? -->

## Checklist

### For new entries
- [ ] Entry file is at `data/beings/<id>.yaml` with id matching filename
- [ ] All seven card properties coded
- [ ] All eleven metadata fields filled in
- [ ] `sequel_link` and `link_type` set (or null)
- [ ] `notes` field explains close calls and distinctive features
- [ ] Validator passes: `python schema/validate.py data/beings/<id>.yaml`
- [ ] Source text read/watched/played (not coded from summaries)
- [ ] Checked [docs/coding_guide.md](docs/coding_guide.md) for judgment-call properties
- [ ] Checked [data/exclusions.yaml](data/exclusions.yaml) — entity not already excluded
- [ ] Influence graph edges added if applicable

### For corrections
- [ ] Re-coding rationale documented in `notes`
- [ ] Textual evidence cited for the change
- [ ] Validator passes after edit

### For all PRs
- [ ] `python schema/validate.py` passes (full corpus)
- [ ] `python analysis/analyze.py --all` runs without error
- [ ] No unrelated changes included

## Notes

<!-- Anything the reviewer should know — boundary case concerns, low-confidence flags, related entries that might need re-review. -->
