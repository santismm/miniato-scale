"""Deterministic synthetic checks; no real-incident validation is performed."""
import json
import unittest
from itertools import product
from aira10 import economic_floor, mortality_floor, score_profile, score_bounds, classify_record

class AiraTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(score_profile([0]*6), 0)
    def test_non_compensation(self):
        self.assertEqual(score_profile([5,3,2,4,0,0]), 5)
    def test_human_extinction(self):
        self.assertEqual(score_profile([8]*6, "human_extinction"), 9)
    def test_ecological_terminal(self):
        self.assertEqual(score_profile([8]*6, "complex_ecosystem_collapse"), 9)
    def test_total_annihilation(self):
        self.assertEqual(score_profile([8]*6, "total_biological_annihilation"), 10)
    def test_no_accidental_terminal(self):
        self.assertEqual(score_profile([8]*6), 8)
    def test_mortality_boundaries(self):
        pairs = [(0,0),(1,5),(9,5),(10,6),(999,6),(1000,7),(999999,7),(1000000,8)]
        for n, expected in pairs:
            self.assertEqual(mortality_floor(n), expected)
    def test_economic_boundaries(self):
        self.assertEqual(economic_floor("0"),0)
        self.assertEqual(economic_floor("0.01"),1)
        for i, exponent in enumerate((3,5,7,9,11,13), 2):
            boundary = 10**exponent
            self.assertEqual(economic_floor(boundary-1),i-1)
            self.assertEqual(economic_floor(boundary),i)
            self.assertEqual(economic_floor(boundary+1),i)
    def test_negative_and_nonfinite(self):
        for value in (-1, "NaN", "Infinity", "wrong", True, 1.5):
            with self.assertRaises(ValueError): economic_floor(value)
        for value in (-1, 1.5, True):
            with self.assertRaises(ValueError): mortality_floor(value)
    def test_invalid_profiles(self):
        for scores in ([0]*5, [0]*7, [9]*6, [-1]*6, [True]*6, [1.1]*6):
            with self.assertRaises(ValueError): score_profile(scores)
    def test_breach_inconsistency(self):
        with self.assertRaises(ValueError): score_profile([0]*6, effective_breach=True)
        self.assertEqual(score_profile([0,0,0,1,0,0], effective_breach=True),1)
    def test_missing_is_not_zero(self):
        result=score_bounds([None]*6,["none"])
        self.assertEqual(result["possible_levels"],list(range(9)))
        self.assertEqual(result["classification"],"set_valued")
    def test_bounds(self):
        result=score_bounds([[5,5],[0,0],[2,4],[0,0],[0,0],[0,0]],["none"])
        self.assertEqual(result["possible_levels"],[5])
    def test_terminal_uncertainty(self):
        result=score_bounds([[8,8]]*6,["none","human_extinction"])
        self.assertEqual(result["possible_levels"],[8,9])
    def test_breach_bounds(self):
        result=score_bounds([None]*6,["none"],effective_breach=True)
        self.assertEqual(result["lower_bound"],1)
    def test_invalid_bounds(self):
        with self.assertRaises(ValueError): score_bounds([[2,1]]*6,["none"])
        with self.assertRaises(ValueError): score_bounds([None]*6,[])
        with self.assertRaises(ValueError): score_bounds([[0,0]]*6,["none"],effective_breach=True)
    def test_metadata_independence(self):
        base={"bounds":[[5,5],[3,3],[2,2],[4,4],[0,0],[0,0]],"terminal_candidates":["none"]}
        for e,a,c in product(range(5),range(5),range(4)):
            result=classify_record({**base,"metadata":{"E":e,"A":a,"C":c}})
            self.assertEqual(result["possible_levels"],[5])
    def test_bad_terminal(self):
        with self.assertRaises(ValueError): score_profile([0]*6,"unknown")
        with self.assertRaises(ValueError): score_bounds([None]*6,["unknown"])
    def test_campaign_raw_aggregation(self):
        self.assertEqual(economic_floor(sum([90000]*100)),3)
        self.assertEqual(economic_floor(sum([90000]*112)),4)
    def test_profile_permutation(self):
        self.assertEqual(score_profile([5,3,2,4,0,0]),score_profile([0,4,3,0,2,5]))


def exhaustive_checks():
    vectors=edges=recodings=0
    for scores in product(range(9), repeat=6):
        m=score_profile(scores)
        assert 0 <= m <= 8
        vectors += 1
        # Increasing recoding preserves the maximum on a common ordinal scale.
        assert max(2*x+3 for x in scores)==2*m+3
        assert max(x*x for x in scores)==m*m
        recodings += 2
        for axis,x in enumerate(scores):
            if x < 8:
                nxt=list(scores); nxt[axis]+=1
                m_next=score_profile(nxt)
                assert m <= m_next <= m+1
                edges+=1
    return {"vectors":vectors,"adjacent_monotonicity_checks":edges,"ordinal_recoding_checks":recodings}

if __name__ == "__main__":
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(AiraTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful(): raise SystemExit(1)
    counts=exhaustive_checks()
    report={"rules_version":"pilot-0.1","unit_tests_run":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),**counts,"interpretation":"Synthetic verification of aggregation and pilot numerical routes only; no empirical or inter-rater validation."}
    with open("verification_report.json","w",encoding="utf-8") as f: json.dump(report,f,ensure_ascii=False,indent=2)
    print(json.dumps(report,indent=2))
