from application import app, db
from application.models import Results
import requests
from flask import render_template


@app.route('/')
def index():
    animal = requests.get('http://animal-api:5000/get-animal')                          #this is pulling the response from the animal api - random animal
    noise = requests.post('http://noise-api:5000/noise', json=animal.json())            #this is posting the animal that was pulled above to the requests for noises - the json=is the data that we're sending   
    db.session.add(Results(animal=animal.json()["animal"], noise=noise.json()["noise"]))  #this is splitting the animal from the json object that we've got from the api variable defined above
    db.session.commit()
    results = Results.query.all()
    return render_template('index.html', results = results)                        