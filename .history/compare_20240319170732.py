# def compare_words(solution, guess):
#     if solution == guess:
#         return guess
#     else:
#         output = ""
#         for i in range(len(solution)):
#             if solution[i] == guess[i]:
#                 output = output + solution[i] + " "
#             else:
#                 output = output + "_" + " "
#     return output


green_color = '\033[92m'  # Green
yellow_color = '\033[93m'  # Yellow
reset_color = '\033[0m'  # Reset to default color

def compare_words(solution, guess):
    if solution == guess:
        return guess
    else:
        output = ""
        for i in range(len(solution)):
            if guess[i] in solution:
              if guess[i]
            else:
                output = output + "_" + " "
    return output