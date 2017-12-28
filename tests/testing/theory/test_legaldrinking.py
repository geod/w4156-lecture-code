import unittest
from lectures.testing.theory.legal_drinking import LegalToDrinkCalculatorWithTwoBugs
from lectures.testing.theory.legal_drinking import LegalToDrinkCalculatorWithOneBug
from lectures.testing.theory.legal_drinking import LegalToDrinkCalculatorBugFreeIHope
from lectures.testing.theory.legal_drinking import Nationality
from typing import Tuple


class Test100StatementCoverageTwoBugs(unittest.TestCase):

    def test_legal_drinking(self):
        """
        This one example shows how we can generate 100% statement coverage but still have a bug
        :return:
        """
        self.assertTrue(LegalToDrinkCalculatorWithTwoBugs.is_legal(21, Nationality.American))

    def test_should_be_illegal_drinking(self):
        """
        This one example shows how we can generate 100% statement coverage but still have a bug
        :return:
        """
        self.assertFalse(LegalToDrinkCalculatorWithTwoBugs.is_legal(8, Nationality.American))


class Test100BranchCoverageOneBug(unittest.TestCase):

    def test_legal(self):
        self.assertTrue(LegalToDrinkCalculatorWithOneBug.is_legal(21, Nationality.American))

    def test_illegal(self):
        self.assertFalse(LegalToDrinkCalculatorWithOneBug.is_legal(8, Nationality.American))

    def test_illegal_british(self):
        self.assertFalse(LegalToDrinkCalculatorWithOneBug.is_legal(17, Nationality.British))


class TestConditionCoverageNoBugs(unittest.TestCase):

    def push_assert(self, tple: Tuple):
        legal = LegalToDrinkCalculatorBugFreeIHope.is_legal(tple[0], tple[1])
        self.assertTrue(legal == tple[2])

    def test_legal_american(self):
        cases = [(21, Nationality.American, True),   # hits statement coverage
                 (20, Nationality.American, False),  # hits branch coverage
                 (18, Nationality.British, True),    # hits condition coverage (evaluated to false previously)
                 (17, Nationality.British, False),
                 ]

        map(lambda x: self.push_assert(x[0], x[1]), cases)

if __name__ == '__main__':
    unittest.main()
