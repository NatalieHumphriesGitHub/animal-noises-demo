from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app


class TestView(TestBase):                           #should do this for all the different animals
    def test_get_noise(self):
        response = self.client.post(url_for('noise'), json={"animal":"cow"})   #need to add the json into it
        self.assert200(response)
        self.assertIn(b'moo', response.data)
