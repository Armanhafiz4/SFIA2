from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.routes import Positions

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Positions(strength_type="pace", weakness_type="heading", position_type="winger"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase): 

    def test_position(self):
        with requests_mock.mock() as m:
            m.get('http://football_gen_service_2:5000/strength', text="pace")
            m.get('http://football_gen_service_3:5000/weakness' ,text="dribbling")
            m.post('http://football_gen_service_4:5000/position', json={"pace" : "winger", "dribbling" : "centreback"})
            response = self.client.get(url_for('index'))
            self.assertIn(b'pace', response.data)
            self.assertIn(b'"suited_position:"winger","unsuited_position":centreback"', response.data)