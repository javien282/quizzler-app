import requests
import random

MY_PARAMS = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php', params=MY_PARAMS)
response.raise_for_status()
data = response.json()['results']

question_data = data
