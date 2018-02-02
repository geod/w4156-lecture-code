import unittest

from lectures.testing.tdd.step1_urlvalidator import URLValidator as Step1Validator


class Step1(unittest.TestCase):
    """
    I am slightly abusing the class names here to show the series of logical steps as part of the TDD process
    Hence the copy paste/growing of the code. However, I want you to be able to see the logical progression and
    if I just showed the final code the process would be lost
    """

    def push_assert(self, url, expected):
        valid = Step1Validator.validate_url(url)
        self.assertEqual(valid, expected, "on URL:%s" % url)

    def test_url_validator(self):
        cases = [("http://www.google.com", True),
                 ("http://www.google.com", True),
                 ("clearlynotvalid", False)]

        for c in cases:
            self.push_assert(c[0], c[1])


if __name__ == '__main__':
    unittest.main()
