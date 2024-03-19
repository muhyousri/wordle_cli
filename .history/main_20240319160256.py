import word_api
import compare

LENGHT = 5


# Get a random word from the API
word = word_api.get_random_word(LENGHT)
print(word)


# Guessing the word
guess = input("Guess the word: ").lower()
compare.compare_words(guess, word)
