# Task 3: Analyzing and Displaying Data

import requests
import json

def fetch_pokemon_data(pokemon_list):
    pokemon_list = [name.lower() for name in pokemon_list if name.isalpha()]
    for pokemon in pokemon_list:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 200:
            json_data = response.text
            data = json.loads(json_data)
            print(f"Name: {data['name']}")
            print(f"Abilities: {', '.join([ability['ability']['name'] for ability in data['abilities']])}")
        else:
            print(f'{response.status_code} {response.text}')
            
def calculate_average_weight(pokemon_list):
    pokemon_list = [name.lower() for name in pokemon_list if name.isalpha()]
    total_weight = 0
    for pokemon in pokemon_list:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 200:
            json_data = response.text
            data = json.loads(json_data)
            total_weight += data['weight']
        else:
            print(f'{response.status_code} {response.text}')
    average_weight = total_weight / len(pokemon_list)
    print(f"Average Weight: {average_weight:.2f}")
        
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
fetch_pokemon_data(pokemon_names)
calculate_average_weight(pokemon_names)