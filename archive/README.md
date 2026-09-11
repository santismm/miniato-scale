# Archive — superseded versions

Kept for traceability. **Do not cite as current.** The design history and the reasons for each change are in [`docs/historia-del-diseno.md`](../docs/historia-del-diseno.md).

| Version | Date | Status | Why superseded |
|---|---|---|---|
| `v0-SMM/` — Escala Santa María Morales 2.1. Continuous 0.0–10.0 with hard caps: 2.0 for purely digital incidents, 3.0 without fatalities. | Sept 2026 | withdrawn | Caps were normative choices presented as mathematics. No scoring function was defined. The "logarithmic" claim was undefined. The CRV modifier was unfalsifiable. The annex mixed verified and unverified cases. See [`docs/critica-v0.md`](../docs/critica-v0.md). |
| `v1-AIRA-10/` — AIRA-10 v1.0, rules `pilot-0.1`. Paper (PDF, DOCX) and reproducible package. | 11 Sept 2026 | superseded | Realistic incidents compressed into levels 0–3. First fatality at level 5. Mortality and economic routes with inconsistent implied ratios. No rule for evaluation-contained incidents. Control flag not mandated. The author's own application of the rules violated them. See [`docs/critica-v1.md`](../docs/critica-v1.md). |
| `v2.0-AIRA-10/` — v2.0 compiled paper under the name AIRA-10, rules `pilot-0.2`. Identical rules to the current version; only the name, the author signature and the AI declaration changed in v2.1. | 12 Sept 2026 | renamed | AIRA is already used by several unrelated AI risk-assessment frameworks; a public scale needs a proper name. See `docs/decisiones.md` D15. |

The v1 reproducible package still runs (`python3 test_aira10.py` inside `material_reproducible/`) and reproduces its own `verification_report.json` byte for byte. That was checked on 11 September 2026 with Python 3.14.
