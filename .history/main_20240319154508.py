import requests


url = 'https://random-word-api.herokuapp.com/word?length=5'
response = requests.get(url)
data = response.text
