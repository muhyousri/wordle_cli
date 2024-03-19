def compare_words(solution, guess):
    print(solution)
    print(guess)
    if solution == guess:
        return "WINNER!"
    else:
        output = ""
        for i in range(len(solution) - 1):
            if solution[i] == guess[i]:
                output += solution[i]
            else:
                output += "-"
    return output
