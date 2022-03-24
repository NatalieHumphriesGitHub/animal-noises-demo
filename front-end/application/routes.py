from application import app
import requests

@app.route('/')
def index():
    animal = requests.get('http://animal-api:5000/get-animal')                          #this is pulling the response from the animal api - random animal
    noise = requests.post('http://noise-api:5000/noise', json=animal.json())            #this is posting the animal that was pulled above to the requests for noises - the json=is the data that we're sending
    return f'{animal.json()["animal"]} goes {noise.json()["noise"]}'                    #this is returning the animal dictionary(json) so we are pulling out the animal value i.e. cow because the json will return "animal:cow" and we just want the animal