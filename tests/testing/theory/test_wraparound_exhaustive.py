import unittest
from lectures.testing.theory.wrap_around_counter import WrapAroundCounter


class MyTestCase(unittest.TestCase):
    """
    A (overly) verbose but basic example of writing test cases for a wrap around counter.
    """

    def test_exhaustive(self):
        self.wrap_around_counter = WrapAroundCounter(5)

        value = self.wrap_around_counter.increment(1)
        self.assertEqual(value, 2)

        value = self.wrap_around_counter.increment(2)
        self.assertEqual(value, 3)

        value = self.wrap_around_counter.increment(3)
        self.assertEqual(value, 4)

        value = self.wrap_around_counter.increment(5)
        self.assertEqual(value, 1)

        value = self.wrap_around_counter.increment(6)
        self.assertEqual(value, 1)

        value = self.wrap_around_counter.increment(0)
        self.assertEqual(value, 1)

        value = self.wrap_around_counter.increment(-1)
        self.assertEqual(value, 1)


if __name__ == '__main__':
    unittest.main()
