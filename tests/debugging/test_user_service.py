import os
import unittest
import tempfile
import json
import lectures.debugging.user_service as service
from lectures.debugging.user_service import app, init_db


# https://damyanon.net/flask-series-testing/
# http://flask.pocoo.org/docs/0.12/testing/
class ApplicationTests(unittest.TestCase):

    one_direction = ["Niall", "Liam", "Louis", "Harry"]

    def assertSuccess(self, res):
        self.assertEqual(res.status, '200 OK')
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def assertFailure(self, res):
        self.assertEqual(res.status, '200 OK')
        data = json.loads(res.data)
        self.assertFalse(data['success'])

    def assertCount(self, res, count):
        self.assertSuccess(res)
        data = json.loads(res.data)
        self.assertEqual(data['count'], count)

    def setUp(self):
        self.db_fd, service.app.config['DATABASE'] = tempfile.mkstemp()
        service.app.config['TESTING'] = True
        self.app = app.test_client()
        with service.app.app_context():
            service.init_db()

    def test_connect(self):
        res = self.app.get('/')
        self.assertEqual(res.status, '200 OK')

    def test_create_user(self, name="brian"):
        res = self.app.get("/createuser/" + name)
        self.assertSuccess(res)

        res = self.app.get("/countusers")
        self.assertCount(res, 1)

    def test_create_duplicate_user(self):
        res = self.app.get("/createuser/brian")
        res = self.app.get("/createuser/brian")
        self.assertFailure(res)

    def test_list_users(self):
        for u in self.one_direction:
            res = self.app.get("/createuser/" + u)

        res = self.app.get("/listusers")
        self.assertSuccess(res)

        data = json.loads(res.data)
        self.assertEquals(data['users'], self.one_direction)

        res = self.app.get("/countusers")
        self.assertCount(res, 4)

    # def test_w4156(self):
    #     # Committed and it should fail
    #     res = self.app.get("/createuser/" + "ryan")
    #     res = self.app.get("/countusers")
    #     self.assertCount(res, 1)
    #
    #     res = self.app.get("/countusers")
    #     self.assertCount(res, 1)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(service.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()