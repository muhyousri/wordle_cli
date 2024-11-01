green_color = '\033[92m'  # Green
yellow_color = '\033[93m'  # Yellow
red_color = '\033[91m'  # Red
reset_color = '\033[0m'  # Reset to default color


def compare_words(solution, guess):
    result = "lose"
    output = ""
    if solution == guess:
        for i in range(len(solution)):
            output = output + green_color + \
                guess[i] + " " + reset_color
            result = "win"
    else:
        for i in range(len(solution)):
            if guess[i] in solution:
                if guess[i] == solution[i]:
                    output = output + green_color + \
                        guess[i] + " " + reset_color
                else:
                    output = output + yellow_color + \
                        guess[i] + " " + reset_color
            else:
                output = output + red_color + guess[i] + " " + reset_color
    return output, result
