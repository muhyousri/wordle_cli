import requests


def get_random_word(lenght):
    url = f'https://random-word-api.herokuapp.com/word?length={lenght}'
    response = requests.get(url)
    return response.text
