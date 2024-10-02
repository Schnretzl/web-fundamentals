# Task 2: Fetching Data from the Pokémon API

import requests
import json

def fetch_pokemon(pokemon_name):
    pokemon_name = pokemon_name.lower()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.status_code == 200:
        json_data = response.text
        data = json.loads(json_data)
        print(f"Name: {data['name']}")
        print(f"Abilities: {', '.join([ability['ability']['name'] for ability in data['abilities']])}")
    else:
        print(f'{response.status_code} {response.text}')
        
fetch_pokemon("pikachu")