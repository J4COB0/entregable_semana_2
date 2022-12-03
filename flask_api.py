from flask import Flask, request
import requests
import sys

app = Flask(__name__)

@app.route('/')
def index():
    """
    This functions handling the operations to do when the route is the home page
    """
    # RETURNING A STATUS SUCCESS IN THE HOME PAGE
    return {'status': 'Success'}, 200

@app.route('/poke')
def poke():
    """
    This functions handling the operations to do when the route is poke
    it get the headers to do a request and return if the ability is in the pokemon
    """
    # GETTING THE HEADERS
    endpoint_poke_api = request.headers['endpoint_poke_api']
    ability_name_header = request.headers['ability_name']
    
    # CHECK IF THE HEADERS ARE NOT EMPTY
    if (not endpoint_poke_api) or (not ability_name_header):
        return {'status': 'error', 'description': 'You need to add the endpoint and the ability name'}, 400

    # GETTING THE RESPONSE BY THE ENDPOINT
    response = requests.get(endpoint_poke_api)
    response = response.json()

    # GETTING THE ABILITY
    abilities = response['abilities'][1]
    ability_name = abilities['ability']['name']

    # COMPARING THE ABILITY
    text = f'The ability {ability_name_header} was not found'
    if ability_name_header in ability_name:
        text = f'The ability {ability_name_header} was found'

    return {'status': 'success', 'ability': text}, 200

@app.route('/status')
def status():
    """
    This functions handling the operations to do when the route is status
    it return and status success with the os and the size of the ram
    """
    # RETURNING THE OS WITH A STATUS 200 SUCCESS
    return {'status': 'success', 'os': sys.platform}, 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)