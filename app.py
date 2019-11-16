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
        pokemonName = request.form.get('pokemon_name')
        pokemonData = requests.get(url = 'https://pokeapi.co/api/v2/pokemon/'+pokemonName)
        data = pokemonData.json()
        print(data['name'])
        return render_template('pokemon.html', name = data['name'])
    return render_template('pokemon.html', name = '')

if __name__ == '__main__':
    app.run()