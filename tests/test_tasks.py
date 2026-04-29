import unittest
from app import app

class TaskTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_tasks(self):
        res = self.client.get('/tasks')
        self.assertIn(res.status_code, [200, 401])

    def test_create_task(self):
        res = self.client.post('/tasks', json={"title": "Task"})
        self.assertIn(res.status_code, [201, 401])