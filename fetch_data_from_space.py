# Task 2: Fetch Data from a Space API
# Task 3: Data Presentation and Analysis

import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return_val = {}

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass_value = planet['mass']['massValue']
            mass_exponent = planet['mass']['massExponent']
            mass = mass_value * (10 ** mass_exponent)
            orbit_period = planet['sideralOrbit']
            return_val[name] = {'mass': mass, 'orbit_period': orbit_period}
    return return_val

def find_heaviest_planet(planet_data):
    heaviest_planet = None
    heaviest_mass = 0
    for planet in planet_data:
        if planet_data[planet]['mass'] > heaviest_mass:
            heaviest_planet = planet
            heaviest_mass = planet_data[planet]['mass']
    return heaviest_planet, heaviest_mass

def find_longest_orbit(planet_data):
    longest_orbit_planet = None
    longest_orbit = 0
    for planet in planet_data:
        if planet_data[planet]['orbit_period'] > longest_orbit:
            longest_orbit_planet = planet
            longest_orbit = planet_data[planet]['orbit_period']
    return longest_orbit_planet, longest_orbit
        
planet_data = fetch_planet_data()
heaviest_planet, heaviest_mass = find_heaviest_planet(planet_data)
longest_orbit_planet, longest_orbit_period = find_longest_orbit(planet_data)
print(f"The heaviest planet is {heaviest_planet} with a mass of {heaviest_mass} kg.")
print(f"The planet with the longest orbit is {longest_orbit_planet} with an orbit period of {longest_orbit_period} days.")