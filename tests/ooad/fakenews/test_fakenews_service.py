import os
import datetime
import unittest
import whois
import requests_mock
from unittest.mock import MagicMock
from tests.ooad.fakenews.test_scorers import MockDomain
import lectures.ooad.fakenews.design3_ok.fake_news_service as fake_news_service
import json

class FlaskrTestCase(unittest.TestCase):
    """
    http://flask.pocoo.org/docs/0.12/testing/

    Admittedly, this is where it gets a bit nasty. We are calling the service (with all the indicators)
    However, we need to mock out each indicator.

    Note - in this test we do NOT need to retest all the functions of each indicator. We have unit tested the indicators
    In this test we want to make sure the service works and is parsing arguments and encoding the response

    Note 2 - an alternate way to implement this test would be to REMOVE most of the indicators within the service.
    This would avoid the need to mock the request and whois. (we would write a mock indicator which would return 0.5)
    """

    def setUp(self):
        fake_news_service.app.testing = True
        fake_news_service.app.config['DATA_DIR'] = os.path.dirname(__file__)
        self.app = fake_news_service.app.test_client()

        fake_news_service.init()

    def test_service(self):
        with requests_mock.Mocker() as mocker:
            '''
            Remember - the scorers make requests. I don't want to have have it actually hit the real websites
            (in unit tests) so I use a fancy feature which mocks what requests (the pyton package will return)
            '''
            mocker.get("http://fooboo.com", text='<html>the response <b> of this devoid</html>')
            whois.query = MagicMock(return_value=MockDomain(datetime.date(2011, 6, 21)))

            # I push in a valid URL and get back a result
            res = self.app.get('/fakenews?newsurl=http://fooboo.com')
            self.assertTrue(res.status_code == 200)

            '''
                Exercise to the student
                1. parse and assert score within range
                2. failure test cases

                NOTE - when it comes to testing we do not need to test each scorer in this test
                Each scorer has already been tested
                In *this* test we are testing it all plugs together and that flask marshalls data in and out correctly
            '''




if __name__ == '__main__':
    unittest.main()
