import unittest
from lectures.testingsamplecode.wrap_around_counter import WrapAroundCounter


class MyTestCase(unittest.TestCase):
    """
    A more realistic example of a test case file. Note the use of setUp which is inherited from unittest.TestCase
    """

    def setUp(self):
        self.wrap_around_counter = WrapAroundCounter(1000)

    def push_assert(self, input, expected):
        """
        A helper method I wrote so I dont have to repeatedly type boring code to push in values and assert.
        Note - you are allowed to write helpers within test cases to make your code more readable
        :param input:
        :param expected:
        :return:
        """
        self.assertEqual(self.wrap_around_counter.increment(input), expected)

    def test_wac(self):
        """
        Remember: any method beginning 'test' will be run and is assumed to contain test cases and assertions
        :return:
        """

        # As personal taste I like the format where you prepare a datastructure with inputs and expected output
        # It makes it very easy to read the test cases.
        cases = [(-1, 1),
                 (0, 1),
                 (1, 2),
                 (999, 1000),
                 (1000, 1),
                 (1001, 1)]

        map(lambda x: self.push_assert(x[0], x[1]), cases)


if __name__ == '__main__':
    unittest.main()
