import unittest


class TestEffficientFrontier(unittest.TestCase):
    """
    This is an exercise to combine our testing theory, EP, BVA, coverage in addition to TDD

    Note - I have also picked a non computer science problem domain which will require understanding a new problem.
    Yes - it may be painful to have to understand a new problem. Yes - this is good practice.

    (Simplifying) When investing there are two key things to consider:
    1. what is the return of the thing you are investing in (what interest rate do you get)
    2. risk - how stable are the returns (or what is the risk you will lose all your money)

    Generally,
    1. the higher the return the higher the risk.
    2. If you could get the same return for lower risk then you would take it (why take more risk for the same return?)
    This latter point this generates what is called the efficient frontier:
    http://www.investinganswers.com/financial-dictionary/investing/efficient-frontier-1010

    As an example, you have four friends who all want to let you invest in their business ventures
        1. Bob - offers you 6% return with 3 std dev return
        2. Alice - offers 2% return with 1 std dev return
        3. Greg - offers 6% return with 2 std dev return
        4. James - offers 8% return with 4 std dec return

    The one that stands out is Bob and Greg. They offer the same return but Bob has higher risk (3 std dev vs 2 std dev)
    Therefore it makes no sense to invest in Greg. He is not on the "efficient frontier".
    Alice offers low returns (but also lowest risk). James offers highest returns with highest risk.

    The efficient frontier would therefore be Alice, Greg, James

    Your tasks is to write a class that takes as input a list of tuples. Each tuple represents return and risk
    [(return3, risk3),(return3, risk3),(return3, risk3),...]

    It should return a set of 'optimal' set of investments sorted from lowest return to highest return.
    """

    def test_pareto(self):
        """
        Follow TDD to fill this in
        0. Think about behavior and devise test cases
        (remember we can not test exhausively so think of equivalence partitions)

        1. Write the test cases
        2. Run the tests (it will fail)
        3. Write just enough code
        3b. Run the tests

        If they do not pass: GOTO 3

        If they pass: Refactor the code if required
        GOTO 2

        Run test coverage. Inspect the coverage and make a decision about whether test suite is 'adequate'
        """
        pass


if __name__ == '__main__':
    unittest.main()
