import unittest
import inspect
from lectures.testing.tdd.step1_urlvalidator import URLValidator as Step1Validator
from lectures.testing.tdd.step2_urlvalidator import URLValidator as Step2Validator


class Step2(unittest.TestCase):
    """
    I am slightly abusing the class names here to show the series of logical steps as part of the TDD process
    Hence the copy paste/growing of the code. However, I want you to be able to see the logical progression and
    if I just showed the final code the process would be lost
    """
    def setUp(self):
        self.url_validator = Step2Validator()

    def push_assert(self, url, expected):
        if inspect.isclass(expected) and issubclass(expected, Exception):
            with self.assertRaises(expected):
                valid = self.url_validator.validate_url(url)
        else:
            valid = self.url_validator.validate_url(url)
            self.assertEqual(valid, expected, "on URL:%s" % url)

    def test_url_validator(self):
        cases = [("", ValueError),
                 ("http://www.google.com", True),
                 ("https://www.google.com/", True),
                 ("clearlynotvalid", ValueError),
                 ("http://validbutnocontent.com", False)]

        for c in cases:
            self.push_assert(c[0], c[1])

if __name__ == '__main__':
    unittest.main()
