import word_api
import compare
import sys


LENGHT = 5


# Get a random word from the API
word = word_api.get_random_word(LENGHT)
print(word)


# Guessing the word - 5 tries only
all_guesses = ""
for i in range(5):
    guess = input("Guess the word: ").lower()
    result = compare.compare_words(word, guess)
    if result[1] == "win":
        all_guesses += result + "\n"
        print(all_guesses)
        print("You win!")
        sys.exit(0)
    else:
        all_guesses += result + "\n"
        print(all_guesses)


print(f"5 tries only. You lost, the word was: {word}")
sys.exit(0)
