import unittest
from lectures.testing.theory.mood_calculator import MoodCalculator


class MyTestCase(unittest.TestCase):
    """
    Note - we have two methods beginning 'test'. Both these methods will be run
    """

    def setUp(self):
        self.mood_calculator = MoodCalculator()

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            self.mood_calculator.calculate_mood(-1, 70)

    def test_mood_calculator(self):
        """
        TODO - Exercise for the student to write and test the mood calculator
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
