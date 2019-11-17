from flask import Flask
from flask import render_template
from flask import request
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def get_pokemon():
    if request.method == 'POST':
        pokemonName = request.form.get('pokemonName')
        pokemonData = requests.get(url = 'https://pokeapi.co/api/v2/pokemon/'+pokemonName)
        data = pokemonData.json()
        print()
        return render_template('pokemon.html', ID = data['id'], name = data['name'], image = data['sprites']['front_default'])
    return render_template('pokemon.html', ID = '', name = '', image = '')

if __name__ == '__main__':
    app.run()