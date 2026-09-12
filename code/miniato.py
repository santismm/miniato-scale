"""Miniato Scale reference implementation, rules pilot-0.3.

Implements the aggregation (max rule + terminal predicates), the health and
economic routes with a single anchor theta, rectangular evidence bounds,
the effective-breach and evaluation-contained rules, and bulletin exceedance
counts. It adjudicates nothing: inputs are levels already established by
human evaluation. Python >= 3.10, standard library only.
"""
from __future__ import annotations
import argparse
import json
from decimal import Decimal, InvalidOperation
from typing import Iterable, Sequence

VERSION = "pilot-0.3"
DOMAINS = ("H", "R", "F", "O", "B", "S")
TERMINALS = ("none", "human_extinction", "complex_ecosystem_collapse", "total_biological_annihilation")
THETA = Decimal(10) ** 7      # euros (2025) per statistical death
INJURY_WEIGHT = Decimal("0.1")  # w: serious permanent injury in harm units


def _level(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 8:
        raise ValueError("Domain levels must be integers from 0 to 8 (not booleans).")
    return value


def _decimal(value: object, name: str) -> Decimal:
    if isinstance(value, (bool, float)):
        raise ValueError(f"{name}: use int, Decimal or decimal string; not bool/float.")
    try:
        amount = Decimal(value)
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f"{name}: invalid amount.") from exc
    if not amount.is_finite() or amount < 0:
        raise ValueError(f"{name}: must be finite and non-negative.")
    return amount


def harm_units(deaths: int, serious_injuries: int = 0, *, w: Decimal = INJURY_WEIGHT) -> Decimal:
    for n in (deaths, serious_injuries):
        if isinstance(n, bool) or not isinstance(n, int) or n < 0:
            raise ValueError("Counts must be non-negative integers.")
    return Decimal(deaths) + w * Decimal(serious_injuries)


def health_floor(deaths: int, serious_injuries: int = 0, *, w: Decimal = INJURY_WEIGHT) -> int:
    """Equation (h). A floor, never a ceiling; zero deaths does not imply H0."""
    u = harm_units(deaths, serious_injuries, w=w)
    if u >= 10 ** 5:
        return 8
    if u >= 10 ** 3:
        return 7
    if u >= 10 ** 2:
        return 6
    if u >= 10:
        return 5
    if u >= 1:
        return 4
    if serious_injuries >= 1:
        return 3
    return 0


def _units_floor(u: Decimal) -> int:
    """Health floor expressed on harm units only (used by the economic route)."""
    if u >= 10 ** 5:
        return 8
    if u >= 10 ** 3:
        return 7
    if u >= 10 ** 2:
        return 6
    if u >= 10:
        return 5
    return 4  # caller guarantees u >= 1


def economic_floor(loss_eur_2025: object, *, theta: Decimal = THETA) -> int:
    """Equation (f). Realised, attributable, deduplicated loss in constant 2025 EUR.
    Every band is proportional to theta, so f is a partition for any theta > 0:
      L >= theta            -> h(L/theta)   (4..8)
      theta/10 <= L < theta -> 3
      theta/100 <= L < theta/10 -> 2
      0 < L < theta/100     -> 1
      L == 0                -> 0
    L includes victims' losses and the necessary cost of restoring or replacing assets
    destroyed or rendered unusable; it excludes response effort, precautionary hardening,
    discretionary upgrades, unrealised exposures and attacker gains (Rule 4)."""
    amount = _decimal(loss_eur_2025, "loss")
    theta = Decimal(theta)
    if theta <= 0:
        raise ValueError("theta must be positive.")
    if amount == 0:
        return 0
    if amount >= theta:
        return _units_floor(amount / theta)
    if amount >= theta / 10:
        return 3
    if amount >= theta / 100:
        return 2
    return 1


def score_profile(scores: Sequence[int], terminal: str = "none", *,
                  effective_breach: bool = False, evaluation_contained: bool = False) -> int:
    """Level of a complete, adjudicated profile (equations max and G)."""
    if len(scores) != 6:
        raise ValueError("Exactly six domain levels are required: H,R,F,O,B,S.")
    levels = [_level(x) for x in scores]
    if terminal not in TERMINALS:
        raise ValueError("Unknown terminal category.")
    if evaluation_contained and effective_breach:
        raise ValueError("An evaluation-contained incident acted within its perimeter; it cannot also be an effective breach.")
    if evaluation_contained and any(levels):
        raise ValueError("Rule 2: an evaluation-contained incident has no realised consequences; profile must be all zeros.")
    if effective_breach:
        levels[3] = max(1, levels[3])  # Rule 1: O >= 1
    if terminal == "total_biological_annihilation":
        return 10
    if terminal != "none":
        return 9
    return max(levels)


def score_bounds(bounds: Sequence[Sequence[int] | None], terminal_candidates: Sequence[str], *,
                 effective_breach: bool = False, evaluation_contained: bool = False) -> dict:
    """Set-valued classification from rectangular domain bounds. Not probabilities."""
    if len(bounds) != 6:
        raise ValueError("Exactly six domain bounds are required.")
    if not terminal_candidates or isinstance(terminal_candidates, str):
        raise ValueError("Provide at least one explicit terminal candidate.")
    if any(x not in TERMINALS for x in terminal_candidates):
        raise ValueError("Unknown terminal candidate.")
    if evaluation_contained and effective_breach:
        raise ValueError("evaluation_contained and effective_breach are mutually exclusive.")
    pairs: list[tuple[int, int]] = []
    for bound in bounds:
        if bound is None:
            pairs.append((0, 8))
            continue
        if len(bound) != 2:
            raise ValueError("Each bound must be [lower, upper] or null.")
        lo, hi = (_level(x) for x in bound)
        if lo > hi:
            raise ValueError("Reversed bounds.")
        pairs.append((lo, hi))
    if evaluation_contained:
        if any(hi > 0 for _, hi in pairs) or set(terminal_candidates) != {"none"}:
            raise ValueError("Rule 2: evaluation-contained incidents have all-zero bounds and no terminal candidates.")
        return _result([0], hazard=True)
    if effective_breach:
        lo, hi = pairs[3]
        if hi < 1:
            raise ValueError("Operational bounds conflict with effective breach (Rule 1 requires O >= 1).")
        pairs[3] = (max(1, lo), hi)
    possible: set[int] = set()
    for terminal in set(terminal_candidates):
        if terminal == "none":
            possible.update(range(max(p[0] for p in pairs), max(p[1] for p in pairs) + 1))
        elif terminal == "total_biological_annihilation":
            possible.add(10)
        else:
            possible.add(9)
    return _result(sorted(possible), hazard=False)


def _result(values: list[int], *, hazard: bool) -> dict:
    return {
        "rules_version": VERSION,
        "possible_levels": values,
        "lower_bound": values[0],
        "upper_bound": values[-1],
        "classification": "point" if len(values) == 1 else "set_valued",
        "hazard_tag": hazard,
        "note": "Evidence-supported ordinal levels; not probabilities or future impacts.",
    }


def control_flag(E: int) -> bool:
    """Public card: flag shown whenever E >= 3 (control not assured)."""
    if isinstance(E, bool) or not isinstance(E, int) or not 0 <= E <= 4:
        raise ValueError("E must be an integer 0..4.")
    return E >= 3


def exceedance_counts(records: Iterable[dict], ks: Sequence[int] = (1, 3, 4, 6)) -> dict:
    """Bulletin counts over consolidated parent records only (Section 9.2).
    Each record: {'lower_bound': int, 'upper_bound': int, 'hazard_tag': bool, 'E': int}."""
    recs = list(records)
    out = {"n_records": len(recs), "certain": {}, "possible": {}, "L_max": 0,
           "hazard_tagged": 0, "control_flagged": 0}
    for k in ks:
        out["certain"][f"N>={k}"] = sum(1 for r in recs if r["lower_bound"] >= k)
        out["possible"][f"N>={k}"] = sum(1 for r in recs if r["upper_bound"] >= k)
    if recs:
        out["L_max"] = max(r["lower_bound"] for r in recs)
    out["hazard_tagged"] = sum(1 for r in recs if r.get("hazard_tag"))
    out["control_flagged"] = sum(1 for r in recs if control_flag(r.get("E", 0)))
    return out


def classify_record(record: dict) -> dict:
    allowed = {"bounds", "terminal_candidates", "effective_breach", "evaluation_contained", "metadata"}
    unknown = set(record) - allowed
    if unknown:
        raise ValueError(f"Unknown top-level fields: {sorted(unknown)}")
    if "bounds" not in record or "terminal_candidates" not in record:
        raise ValueError("bounds and terminal_candidates must be explicit.")
    result = score_bounds(record["bounds"], record["terminal_candidates"],
                          effective_breach=record.get("effective_breach", False),
                          evaluation_contained=record.get("evaluation_contained", False))
    meta = record.get("metadata", {})
    result["metadata"] = meta
    if "E" in meta:
        result["control_flag"] = control_flag(meta["E"])
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", help="Path to a UTF-8 JSON record (or a JSON list of records for bulletin counts).")
    args = parser.parse_args()
    try:
        with open(args.record, encoding="utf-8") as stream:
            data = json.load(stream)
        if isinstance(data, list):
            results = [classify_record(r) for r in data]
            for r in results:
                r["E"] = r.get("metadata", {}).get("E", 0)
            print(json.dumps(exceedance_counts(results), ensure_ascii=False, indent=2))
        else:
            print(json.dumps(classify_record(data), ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, f"Miniato input error: {exc}\n")


if __name__ == "__main__":
    main()
