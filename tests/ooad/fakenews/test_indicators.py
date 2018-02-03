from lectures.ooad.fakenews.design3_ok.indicators import *
import unittest
import requests_mock
from unittest.mock import MagicMock, Mock
from freezegun import freeze_time
import datetime
import os
from tests.ooad.fakenews import TEST_DIR


class AbstractScorerTest(unittest.TestCase):

    def assertScore(self, domain, value):
        score = self._scorer.score_domain(domain)
        self.assertAlmostEqual(score, value, places=2)


class TestContentScorer(AbstractScorerTest):

    def setUp(self):
        # note when unit tests run the home directory is tests/ooad/fakenews
        # this allows us to set a local data file specifically for testing
        self._scorer = ContentScorer(baseconfigdir=os.path.dirname(__file__), filename="keywords.csv")

    @requests_mock.mock()
    def test_content(self, m):
        # domain doesnt matter
        domain_a = "http://domaina.com"
        domain_b = "http://domainb.com"
        domain_c = "http://domainc.com"


        # we mock out the return value of requests
        m.get(domain_a, text='<html> includes <b>nasty</<b> keywords such as work '
                             'from home and you won\'t believe</html>')
        m.get(domain_b, text='<html>the response <b> of this devoid</html>')
        m.get(domain_c, text='')

        # when we call the scorer and it uses 'requests' the method will return what we mocked above
        self.assertScore(domain_a, 0.3)
        self.assertScore(domain_b, 0.5)
        self.assertScore(domain_c, 0.5)


class TestWhitelistScorer(AbstractScorerTest):

    def setUp(self):
        # note when unit tests run the home directory is tests/ooad/fakenews
        # this allows us to set a local data file specifically for testing
        self._scorer = WhitelistScorer(baseconfigdir=os.path.dirname(__file__), filename='whitelist.csv')

    def test_whitelist(self):
        # not in whitelist
        self.assertScore("notinwhitelistfile.com", 0.5)

        # in whitelist
        self.assertScore("reddit.com", 0.6)

        # case insensitivity
        self.assertScore("Reddit.com", 0.6)

        # empty
        self.assertScore("", 0.5)

        # invalid
        with self.assertRaises(ValueError):
            self._scorer.score_domain(None)


class MockDomain:
    def __init__(self, cd):
        self.creation_date = cd


class TestWhoisScorer(AbstractScorerTest):
    """
    https://stackoverflow.com/questions/4481954/python-trying-to-mock-datetime-date-today-but-not-working
    """

    def setUp(self):
        self._scorer = WhoisScorer()

    def test_whois(self):
        with freeze_time("2018-01-01"):
            whois.query = MagicMock(return_value=MockDomain(datetime.date(2011, 6, 21)))
            self.assertScore("verylongtime", 1.0)

            # 0 days
            whois.query = MagicMock(return_value=MockDomain(datetime.date(2018, 1, 1)))
            self.assertScore("zerodays", 0.0)

            # 365
            whois.query = MagicMock(return_value=MockDomain(datetime.date(2017, 1, 1)))
            self.assertScore("oneyear", 0.5)

            # 730
            whois.query = MagicMock(return_value=MockDomain(datetime.date(2016, 1, 1)))
            self.assertScore("oneyear", 1.0)

            # lets be a bit paranoid - forward date
            whois.query = MagicMock(return_value=MockDomain(datetime.date(2018, 1, 2)))
            self.assertScore("forwarddate", 0.0)

if __name__ == '__main__':
    unittest.main()
