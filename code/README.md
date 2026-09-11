# Miniato Scale — reference implementation, rules `pilot-0.2`

Python ≥ 3.10, standard library only. The code adjudicates nothing: it receives domain levels and numeric inputs already established by human evaluation and returns levels, admissible sets, flags and bulletin counts. It does not read incident text, does not use a language model and does not decide emergency priority.

```sh
python3 test_miniato.py                 # 16 unit tests + exhaustive enumeration of 9^6 profiles; writes verification_report.json
python3 miniato.py example_cases.json   # bulletin counts over the six retrospective cases of the paper
```

## API

| Function | Implements |
|---|---|
| `health_floor(deaths, serious_injuries)` | Eq. (6): harm units U = D + 0.1·J; floors 3 to 8. |
| `economic_floor(loss_eur_2025)` | Eq. (7): floors 1 to 8; above θ = 10⁷ € defined through the health route. |
| `score_profile(scores, terminal, effective_breach, evaluation_contained)` | Eqs. (2) and (3), plus Rule 1 (breach ⇒ O ≥ 1) and Rule 2 (evaluation-contained ⇒ 0 with hazard tag). |
| `score_bounds(bounds, terminal_candidates, ...)` | Set-valued classification from rectangular evidence bounds (Section 5.3). |
| `control_flag(E)` | Public card flag: true when E ≥ 3. |
| `exceedance_counts(records)` | Bulletin: N≥k certain and possible, L_max, hazard-tagged and control-flagged counts (Section 9). |

## Record format (`example_cases.json`)

```json
{
  "bounds": [[H_lo, H_hi], [R_lo, R_hi], [F_lo, F_hi], [O_lo, O_hi], [B_lo, B_hi], [S_lo, S_hi]],
  "terminal_candidates": ["none"],
  "effective_breach": false,
  "evaluation_contained": false,
  "metadata": {"id": "...", "E": 0, "A": 0, "C": 0}
}
```

`null` in a bound means unknown and spans 0 to 8; it is never treated as 0. Terminal candidates other than `none` are `human_extinction`, `complex_ecosystem_collapse` and `total_biological_annihilation`; their truth is adjudicated outside the program.

## What the verification proves and what it does not

`verification_report.json` records that the aggregation is bounded, weakly monotone and independent of E, A and C, and that the two numeric routes agree at every boundary above θ. It says nothing about whether the thresholds are right, whether evaluators agree, or whether the public understands the card. Those are the open questions in `docs/hoja-de-ruta.md`.
