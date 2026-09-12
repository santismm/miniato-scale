"""Deterministic synthetic checks for rules pilot-0.3. No real-incident validation."""
import json
import unittest
from decimal import Decimal
from itertools import product
from miniato import (THETA, economic_floor, health_floor, score_profile, score_bounds,
                    classify_record, exceedance_counts, control_flag)


class AiraTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(score_profile([0] * 6), 0)

    def test_non_compensation(self):
        self.assertEqual(score_profile([5, 3, 2, 4, 0, 0]), 5)

    def test_terminals(self):
        self.assertEqual(score_profile([8] * 6, "human_extinction"), 9)
        self.assertEqual(score_profile([8] * 6, "complex_ecosystem_collapse"), 9)
        self.assertEqual(score_profile([8] * 6, "total_biological_annihilation"), 10)
        self.assertEqual(score_profile([8] * 6), 8)

    def test_health_boundaries(self):
        pairs = [(0, 0, 0), (1, 0, 4), (9, 0, 4), (10, 0, 5), (99, 0, 5), (100, 0, 6), (999, 0, 6),
                 (1000, 0, 7), (99999, 0, 7), (100000, 0, 8), (0, 1, 3), (0, 9, 3), (0, 10, 4), (5, 50, 5)]
        for d, j, expected in pairs:
            self.assertEqual(health_floor(d, j), expected, (d, j))

    def test_economic_boundaries(self):
        self.assertEqual(economic_floor("0"), 0)
        self.assertEqual(economic_floor("0.01"), 1)
        cases = {10**5: 2, 10**6: 3, 10**7: 4, 10**8: 5, 10**9: 6, 10**10: 7, 10**12: 8}
        for boundary, level in cases.items():
            self.assertEqual(economic_floor(boundary - 1), level - 1 if boundary != 10**12 else 7)
            self.assertEqual(economic_floor(boundary), level)
            self.assertEqual(economic_floor(boundary + 1), level)
        self.assertEqual(economic_floor(10**11), 7)

    def test_theta_partition(self):
        # For every theta in the sensitivity set, f is monotone in L, gap-free and overlap-free.
        for theta in (Decimal(10)**6, 3*Decimal(10)**6, Decimal(10)**7, 3*Decimal(10)**7):
            self.assertEqual(economic_floor(theta / 100 - 1, theta=theta), 1)
            self.assertEqual(economic_floor(theta / 100, theta=theta), 2)
            self.assertEqual(economic_floor(theta / 10 - 1, theta=theta), 2)
            self.assertEqual(economic_floor(theta / 10, theta=theta), 3)
            self.assertEqual(economic_floor(theta - 1, theta=theta), 3)
            self.assertEqual(economic_floor(theta, theta=theta), 4)
            prev = 0
            for k in range(0, 140):
                L = Decimal(10) ** (Decimal(k) / 10)  # 1 .. 10^13.9
                lvl = economic_floor(L, theta=theta)
                self.assertGreaterEqual(lvl, prev)
                self.assertIn(lvl, range(1, 9))
                prev = lvl
        # The review's two counterexamples against version 2.1 now resolve to one value each.
        self.assertEqual(economic_floor(2_000_000, theta=Decimal(10)**6), 4)
        self.assertEqual(economic_floor(20_000_000, theta=3*Decimal(10)**7), 3)
        with self.assertRaises(ValueError):
            economic_floor(1, theta=Decimal(0))

    def test_single_anchor_alignment(self):
        # For every level >= 4, the economic floor at L = U * theta equals the health floor at U deaths.
        for deaths in (1, 5, 10, 50, 100, 999, 1000, 99999, 100000, 10**7):
            self.assertEqual(economic_floor(Decimal(deaths) * THETA), health_floor(deaths))

    def test_invalid_inputs(self):
        for value in (-1, "NaN", "Infinity", "wrong", True, 1.5):
            with self.assertRaises(ValueError):
                economic_floor(value)
        for value in (-1, 1.5, True):
            with self.assertRaises(ValueError):
                health_floor(value)
        for scores in ([0] * 5, [0] * 7, [9] * 6, [-1] * 6, [True] * 6, [1.1] * 6):
            with self.assertRaises(ValueError):
                score_profile(scores)
        with self.assertRaises(ValueError):
            score_profile([0] * 6, "unknown")

    def test_rule1_breach_floor(self):
        self.assertEqual(score_profile([0] * 6, effective_breach=True), 1)
        self.assertEqual(score_profile([0, 0, 0, 3, 0, 0], effective_breach=True), 3)
        r = score_bounds([None] * 6, ["none"], effective_breach=True)
        self.assertEqual(r["lower_bound"], 1)
        with self.assertRaises(ValueError):
            score_bounds([[0, 0]] * 6, ["none"], effective_breach=True)

    def test_rule2_evaluation_contained(self):
        self.assertEqual(score_profile([0] * 6, evaluation_contained=True), 0)
        r = score_bounds([[0, 0]] * 6, ["none"], evaluation_contained=True)
        self.assertEqual(r["possible_levels"], [0])
        self.assertTrue(r["hazard_tag"])
        with self.assertRaises(ValueError):
            score_profile([0, 0, 0, 1, 0, 0], evaluation_contained=True)
        with self.assertRaises(ValueError):
            score_profile([0] * 6, evaluation_contained=True, effective_breach=True)

    def test_missing_is_not_zero(self):
        r = score_bounds([None] * 6, ["none"])
        self.assertEqual(r["possible_levels"], list(range(9)))
        self.assertEqual(r["classification"], "set_valued")

    def test_bounds_and_terminal_uncertainty(self):
        self.assertEqual(score_bounds([[5, 5], [0, 0], [2, 4], [0, 0], [0, 0], [0, 0]], ["none"])["possible_levels"], [5])
        self.assertEqual(score_bounds([[8, 8]] * 6, ["none", "human_extinction"])["possible_levels"], [8, 9])
        with self.assertRaises(ValueError):
            score_bounds([[2, 1]] * 6, ["none"])
        with self.assertRaises(ValueError):
            score_bounds([None] * 6, [])

    def test_metadata_independence(self):
        base = {"bounds": [[5, 5], [3, 3], [2, 2], [4, 4], [0, 0], [0, 0]], "terminal_candidates": ["none"]}
        for e, a, c in product(range(5), range(5), range(4)):
            r = classify_record({**base, "metadata": {"E": e, "A": a, "C": c}})
            self.assertEqual(r["possible_levels"], [5])
            self.assertEqual(r["control_flag"], e >= 3)

    def test_control_flag(self):
        self.assertEqual([control_flag(e) for e in range(5)], [False, False, False, True, True])
        with self.assertRaises(ValueError):
            control_flag(5)

    def test_campaign_consolidation(self):
        # 112 x 90,000 EUR: each episode F1, consolidated F4.
        self.assertEqual(economic_floor(90000), 1)
        self.assertEqual(economic_floor(90000 * 112), 4)

    def test_exceedance_counts(self):
        recs = [
            {"lower_bound": 0, "upper_bound": 0, "hazard_tag": True, "E": 2},
            {"lower_bound": 1, "upper_bound": 1, "hazard_tag": False, "E": 0},
            {"lower_bound": 3, "upper_bound": 3, "hazard_tag": False, "E": 0},
            {"lower_bound": 4, "upper_bound": 4, "hazard_tag": False, "E": 0},
            {"lower_bound": 5, "upper_bound": 6, "hazard_tag": False, "E": 1},
            {"lower_bound": 2, "upper_bound": 3, "hazard_tag": False, "E": 4},
        ]
        out = exceedance_counts(recs)
        self.assertEqual(out["certain"], {"N>=1": 5, "N>=3": 3, "N>=4": 2, "N>=6": 0})
        self.assertEqual(out["possible"], {"N>=1": 5, "N>=3": 4, "N>=4": 2, "N>=6": 1})
        self.assertEqual(out["L_max"], 5)
        self.assertEqual(out["hazard_tagged"], 1)
        self.assertEqual(out["control_flagged"], 1)

    def test_profile_permutation(self):
        self.assertEqual(score_profile([5, 3, 2, 4, 0, 0]), score_profile([0, 4, 3, 0, 2, 5]))


def exhaustive_checks():
    vectors = edges = 0
    for scores in product(range(9), repeat=6):
        m = score_profile(scores)
        assert 0 <= m <= 8 and m == max(scores)
        vectors += 1
        for axis, x in enumerate(scores):
            if x < 8:
                nxt = list(scores); nxt[axis] += 1
                assert m <= score_profile(nxt) <= m + 1
                edges += 1
    return {"vectors": vectors, "adjacent_monotonicity_checks": edges}


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AiraTests)
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    counts = exhaustive_checks()
    report = {"rules_version": "pilot-0.3", "unit_tests_run": result.testsRun,
              "failures": len(result.failures), "errors": len(result.errors), **counts,
              "interpretation": "Synthetic verification of aggregation, routes and bulletin counts only; no empirical or inter-rater validation."}
    with open("verification_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, indent=2))
