from flask import Flask, escape, request, jsonify
import json

app = Flask(__name__) # create an app instance

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return 'Hello, {escape(name)}!'
                           
@app.route('/pokedex', methods=['GET'])
def view_pokedex():
    return jsonify(pokedex.list())         

@app.route('/<name>', methods=['GET'])
def view_pokemon(name):
    return jsonify(pokedex[name].list())
        
if __name__ == 'main':
    pokedex = request.get('pokemon.json')
    app.run(debug=True)
