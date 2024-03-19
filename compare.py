def compare_words(solution, guess):
    if solution == guess:
        return guess
    else:
        output = ""
        for i in range(len(solution)):
            if solution[i] == guess[i]:
                output = output + solution[i] + " "
            else:
                output = output + "_" + " "
    return output
