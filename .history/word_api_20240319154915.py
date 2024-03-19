import requests


def get_random_word():
    url = 'https://random-word-api.herokuapp.com/word?length=5'
    response = requests.get(url)
    return response.text
