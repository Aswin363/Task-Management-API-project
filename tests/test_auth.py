import unittest
from app import app

class AuthTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_register(self):
        res = self.client.post('/Auth/register', json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Abcd1"
        })
        self.assertEqual(res.status_code, 201)

    def test_login(self):
        res = self.client.post('/Auth/login', json={
            "username": "test",
            "password": "Abcd1"
        })
        self.assertEqual(res.status_code, 200)