import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b5b203e48e3b3da0ea4457c957527512'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "168587",
    "name": "Olik",
    "photo_id": 1
}

body_pokeboll = {
    "pokemon_id": "168587"
}

"""response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)"""

"""response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print(response_change.text)"""


response_pokeboll = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeboll)
print(response_pokeboll.text)



