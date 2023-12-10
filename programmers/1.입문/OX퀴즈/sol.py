def solution(quiz):
    answer = []

    for i in range(len(quiz)):
        quiz[i] = quiz[i].replace(' ', '')
        equal_sign = quiz[i].find('=')
        for char in quiz[i][:equal_sign]:
            if char == '+':
                idx = quiz[i].find('+')
                if int(quiz[i][:idx])+int(quiz[i][idx+1:equal_sign]) == int(quiz[i][equal_sign+1:]):
                    answer.append('O')
                else:
                    answer.append('X')
            elif char == '-':
                idx = quiz[i].find('-')
                if int(quiz[i][:idx])-int(quiz[i][idx+1:equal_sign]) == int(quiz[i][equal_sign+1:]):
                    answer.append('O')
                else:
                    answer.append('X')

    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))