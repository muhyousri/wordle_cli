import requests


def get_random_word(lenght):
    """
    Get a random word from the API
    :param lenght: the lenght of the word
    :return: the word
    """
    return get_random_word_from_api(lenght)
    url = f'https://random-word-api.herokuapp.com/word?length={lenght}'
    response = requests.get(url)
    return response.text[2:-2]
