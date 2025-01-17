from application import app, db
from application.models import Results
from flask import url_for
import requests_mock
from flask_testing import TestCase      

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',  #setting a local db file for testing
            DEBUG = True
        )
        return app

    def setUp(self):
        sample_result = Results(animal='cat', noise='meow')             #setting up a sample table for the testing and adding to the local db
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestView(TestBase):    #if you have multiple get requests to test, you can't use patch, so instead you should use mocker
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:                                       #creating a mocker object
            m.get('http://animal-api:5000/get-animal', json={"animal":"dog"})   #this mocking our get request
            m.post('http://noise-api:5000/noise', json={"noise":"woof"})        #this is mocking our post request
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'cat goes meow', response.data) #this is the sample that we added at the top
            self.assertIn(b'dog goes woof', response.data)