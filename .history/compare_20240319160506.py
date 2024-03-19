def compare_words(solution, guess):

    if solution == guess:
        return "WINNER!"
    else:
        for i in range(len(solution)):
            if solution[i] == guess[i]:
                return i
            else:
                return "_"
