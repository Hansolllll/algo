def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        # 등호 찾아서 등호 이전부분과 이후부분 나누기
        equal_sign = quiz[i].find('=')
        before = quiz[i][:equal_sign]
        before = before.split(' ')
        after  = quiz[i][equal_sign+1:]
        # - 기호 있다면 첫번째 원소랑 두번째 원소 차이 구해서 after와 비교
        if '-' in before:
            before.remove('-')
            if int(before[0]) - int(before[-2]) == int(after):
                answer.append('O')
            else:
                answer.append('X')

        # + 기호 있다면 첫번째 원소랑 두번째 원소 합 구해서 after와 비교
        elif '+' in before:
            before.remove('+')
            if int(before[0]) + int(before[-2]) == int(after):
                answer.append('O')
            else:
                answer.append('X') 

    return answer
        

    # 런타임 에러
    # for i in range(len(quiz)):
    #     quiz[i] = quiz[i].replace(' ', '')
    #     equal_sign = quiz[i].find('=')
    #     for char in quiz[i][:equal_sign]:
    #         if char == '+':
    #             idx = quiz[i].find('+')
    #             if int(quiz[i][:idx])+int(quiz[i][idx+1:equal_sign]) == int(quiz[i][equal_sign+1:]):
    #                 answer.append('O')
    #             else:
    #                 answer.append('X')
    #         elif char == '-':
    #             idx = quiz[i].find('-')
    #             if int(quiz[i][:idx])-int(quiz[i][idx+1:equal_sign]) == int(quiz[i][equal_sign+1:]):
    #                 answer.append('O')
    #             else:
    #                 answer.append('X')

    # return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))