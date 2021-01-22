from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from application import app
from random import choice, randint


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_strength(self):
            with patch("random.choice") as random:
                random.return_value = "pace"
                response = self.client.get(url_for('get_strength'))
                self.assertIn(b'pace', response.data)

            for _ in range(10):
                response = self.client.get(url_for('get_strength'))
                self.assertIn(response.data, [b"pace", b"defending", b"shooting"])

    