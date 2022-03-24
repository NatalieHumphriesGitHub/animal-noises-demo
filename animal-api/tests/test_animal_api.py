from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for


class TestBase(TestCase):                   #this sets up the app
    def create_app(self):
        return app

class TestView(TestBase):

    def test_get_animal_cat(self):                          #mocking the choice function
        with patch('application.routes.choice') as r:   #r = the patch function - #need to ensure that routes is imported and that random import choice has happened in routes
            r.return_value = 'cat'             
            response = self.client.get(url_for('get_animal')) # this is checking that the response is the url for get animal
            self.assert200(response)                           #checking that there is a successful response
            self.assertIn(b'cat', response.data)                #ideally you should have a test for each random thing that you're going to have returned

    @patch('application.routes.choice', return_value = 'dog')  #this is the same as above, but just neater syntax - called a decorator
    def test_get_animal_dog(self, mock_function):                            
            response = self.client.get(url_for('get_animal')) 
            self.assert200(response)                          
            self.assertIn(b'dog', response.data)               