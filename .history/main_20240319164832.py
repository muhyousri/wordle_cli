import word_api
import compare

LENGHT = 5


# Get a random word from the API
word = word_api.get_random_word(LENGHT)
print(word)


# Guessing the word - 5 tries only

all_guesses = ""
for i in range(5):
    guess = input("Guess the word: ").lower()
    result = compare.compare_words(guess, word)
    all_guesses += result + "\n"
    if result == "WINNER!":
        print("You win!")
        break
    else:
        print(all_guesses)


print(f"5 tries only. You lost, the word was: {word}")
