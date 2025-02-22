import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b5b203e48e3b3da0ea4457c957527512'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '13340'


def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID })
    assert response.status_code == 200
    