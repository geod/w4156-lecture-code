import os
import lectures.ooad.fakenews.design3_ok.fake_news_service as fake_news_service
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):
    """
    http://flask.pocoo.org/docs/0.12/testing/
    """

    def setUp(self):
        fake_news_service.app.testing = True
        self.app = fake_news_service.app.test_client()

    def test_url(self):
        pass

    def test_error(self):
        pass


if __name__ == '__main__':
    unittest.main()
