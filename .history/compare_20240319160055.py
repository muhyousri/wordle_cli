def compare(solution, guess):
    if solution == guess:
        return "WINNER!"
    elif:
        for i in range(len(solution)):
            if solution[i] == guess[i]:
                return i
            else:
                return "_"
