import word_api

LENGHT = 5


# Get a random word from the API
word = word_api.get_random_word(LENGHT)


# guessing the word
guess = input("Guess the word: ").lower()
