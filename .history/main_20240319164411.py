import word_api
import compare

LENGHT = 5


# Get a random word from the API
word = word_api.get_random_word(LENGHT)
print(word)


# Guessing the word


for i in range(4):
    guess = input("Guess the word: ").lower()
    result = compare.compare_words(guess, word)
    if result == "WINNER!":
        print("You win!")
        break



