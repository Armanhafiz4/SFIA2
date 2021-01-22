from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestResponse(TestBase):
    def test_get_position(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "pace", "weakness" : "passing"})
        print(response)
        self.assertIn(b'"suited_position":"winger","unsuited_position":"striker"', response.data)
    def test_get_position2(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "pace", "weakness" : "dribbling"})
        print(response)
        self.assertIn(b'"suited_position":"winger","unsuited_position":"centreback"', response.data)
    def test_get_position3(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "pace", "weakness" : "heading"})
        print(response)
        self.assertIn(b'"suited_position":"winger","unsuited_position":"winger"', response.data)
    def test_get_position4(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "defending", "weakness" : "passing"})
        print(response)
        self.assertIn(b'"suited_position":"centreback","unsuited_position":"striker"', response.data)
    def test_get_position5(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "defending", "weakness" : "dribbling"})
        print(response)
        self.assertIn(b'"suited_position":"centreback","unsuited_position":"centreback"', response.data)
    def test_get_position6(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "defending", "weakness" : "heading"})
        print(response)
        self.assertIn(b'"suited_position":"centreback","unsuited_position":"winger"', response.data)
    def test_get_position7(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "shooting", "weakness" : "passing"})
        print(response)
        self.assertIn(b'"suited_position":"striker","unsuited_position":"striker"', response.data)
    def test_get_position8(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "shooting", "weakness" : "dribbling"})
        print(response)
        self.assertIn(b'"suited_position":"striker","unsuited_position":"centreback"', response.data)
    def test_get_position9(self):
        response = self.client.post(url_for('get_position'), json={"strength" : "shooting", "weakness" : "heading"})
        print(response)
        self.assertIn(b'"suited_position":"striker","unsuited_position":"winger"', response.data)