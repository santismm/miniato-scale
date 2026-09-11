"""AIRA-10 research reference implementation (rules pilot-0.1).

Implements aggregation and the two quantitative pilot routes, NOT automated
fact finding, causality, expert domain rubrics, or emergency prioritisation.
Python >= 3.10; standard library only. No network or file mutation beyond CLI output.
"""
from __future__ import annotations
import argparse
import json
from decimal import Decimal, InvalidOperation
from typing import Sequence

VERSION = "pilot-0.1"
DOMAINS = ("H", "R", "F", "O", "B", "S")
TERMINALS = ("none", "human_extinction", "complex_ecosystem_collapse", "total_biological_annihilation")


def _level(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 8:
        raise ValueError("Domain levels must be integers from 0 to 8 (not booleans).")
    return value


def mortality_floor(deaths: int) -> int:
    """Mortality route only: zero deaths does not imply zero health impact."""
    if isinstance(deaths, bool) or not isinstance(deaths, int) or deaths < 0:
        raise ValueError("Deaths must be a non-negative integer.")
    if deaths == 0:
        return 0
    if deaths < 10:
        return 5
    if deaths < 1_000:
        return 6
    if deaths < 1_000_000:
        return 7
    return 8


def economic_floor(loss_eur_2025: str | int | Decimal) -> int:
    """Realised, attributable loss in constant 2025 euros; a pilot convention."""
    if isinstance(loss_eur_2025, (bool, float)):
        raise ValueError("Use an integer, Decimal, or decimal string; not bool/float.")
    try:
        amount = Decimal(loss_eur_2025)
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError("Invalid monetary amount.") from exc
    if not amount.is_finite() or amount < 0:
        raise ValueError("Loss must be finite and non-negative.")
    if amount == 0:
        return 0
    boundaries = [Decimal(10) ** e for e in (3, 5, 7, 9, 11, 13)]
    return 1 + sum(amount >= boundary for boundary in boundaries)


def score_profile(scores: Sequence[int], terminal: str = "none", *, effective_breach: bool = False) -> int:
    """Score a complete, already adjudicated profile; no evidence inference.

    'none' means terminal criteria have been excluded for the scoped incident,
    not merely that nobody has assessed them. A true effective_breach requires
    a documented operational-integrity floor of at least O1.
    """
    if len(scores) != 6:
        raise ValueError("Exactly six domain levels are required: H,R,F,O,B,S.")
    levels = tuple(_level(x) for x in scores)
    if terminal not in TERMINALS:
        raise ValueError("Unknown terminal category.")
    if not isinstance(effective_breach, bool):
        raise ValueError("effective_breach must be boolean.")
    if effective_breach and levels[3] == 0:
        raise ValueError("An effective control breach requires O >= 1.")
    if terminal == "total_biological_annihilation":
        return 10
    if terminal != "none":
        return 9
    return max(levels)


def score_bounds(bounds: Sequence[Sequence[int] | None], terminal_candidates: Sequence[str], *, effective_breach: bool = False) -> dict:
    """Set-valued evidence, not probabilities. Each null domain spans 0..8.

    Caller supplies evidence-supported candidates for present consequences,
    not worst-case future scenarios. Bounds are rectangular; correlated
    evidence requires a caller-supplied joint feasible-set implementation.
    """
    if len(bounds) != 6:
        raise ValueError("Exactly six domain bounds are required.")
    if not terminal_candidates or isinstance(terminal_candidates, str):
        raise ValueError("Provide at least one explicit terminal candidate.")
    if any(x not in TERMINALS for x in terminal_candidates):
        raise ValueError("Unknown terminal candidate.")
    pairs = []
    for bound in bounds:
        if bound is None:
            pairs.append((0, 8))
        else:
            if len(bound) != 2:
                raise ValueError("Each bound must be [lower, upper] or null.")
            lo, hi = (_level(x) for x in bound)
            if lo > hi:
                raise ValueError("Reversed bounds.")
            pairs.append((lo, hi))
    if not isinstance(effective_breach, bool):
        raise ValueError("effective_breach must be boolean.")
    if effective_breach:
        lo, hi = pairs[3]
        if hi < 1:
            raise ValueError("Operational bounds conflict with effective breach.")
        pairs[3] = (max(1, lo), hi)
    possible: set[int] = set()
    for terminal in set(terminal_candidates):
        if terminal == "none":
            possible.update(range(max(p[0] for p in pairs), max(p[1] for p in pairs) + 1))
        elif terminal == "total_biological_annihilation":
            possible.add(10)
        else:
            possible.add(9)
    values = sorted(possible)
    return {
        "rules_version": VERSION,
        "possible_levels": values,
        "lower_bound": values[0],
        "upper_bound": values[-1],
        "classification": "point" if len(values) == 1 else "set_valued",
        "note": "Evidence-supported ordinal levels; not probabilities or future impacts.",
    }


def classify_record(record: dict) -> dict:
    """Minimal CLI adapter. Metadata E/A/C is returned, never averaged in."""
    allowed = {"bounds", "terminal_candidates", "effective_breach", "metadata"}
    unknown = set(record) - allowed
    if unknown:
        raise ValueError(f"Unknown top-level fields: {sorted(unknown)}")
    if "bounds" not in record or "terminal_candidates" not in record:
        raise ValueError("bounds and terminal_candidates must be explicit.")
    result = score_bounds(record["bounds"], record["terminal_candidates"], effective_breach=record.get("effective_breach", False))
    result["metadata"] = record.get("metadata", {})
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", help="Path to a UTF-8 JSON record.")
    args = parser.parse_args()
    try:
        with open(args.record, encoding="utf-8") as stream:
            data = json.load(stream)
        result = classify_record(data)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, f"AIRA-10 input error: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
