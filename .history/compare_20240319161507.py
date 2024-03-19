def compare_words(solution, guess):
    print(solution)
    print(guess)
    if solution == guess:
        return "WINNER!"
    else:
        for i in range(len(solution) - 1):
            if solution[i] == guess[i]:
                return solution[i]
            else:
                return "_"
