from application import app
from flask import request, jsonify                          #request allows us to do get etc requests and jsonify allows us to use josn

noises = dict(cow='moo', dog='woof', sheep='baa', cat='meow', pig='oink')

@app.route('/noise', methods=['POST'])
def noise():
    animal_json = request.get_json()                        #this is a get request asking for all the animals
    animal = animal_json["animal"]                          #this is defining that animal = "animal" from the above get request
    return jsonify(noise=noises[animal])                    #this is returning the noise using the animal as a key for the noises dictionary