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

# 풀이 2
def solution(quiz):
    answer = []
    for i in quiz:
        a = i.split()  #["3' '-' '4' '=' '-3"],['5', '+', '6', '=', '11']
        if a[1] == "-":
            if int(a[0]) - int(a[2]) == int(a[-1]):
                answer.append('O')
            else:
                answer.append('X')

        if a[1] == "+":
            if int(a[0] )+ int(a[2]) == int(a[-1]):
                answer.append('O')
            else:
                answer.append('X')

    return answer

# eval 이용
def solution(quiz):
    result = []
    answer = []
    for char in range(len(quiz)):
        result.append(quiz[char].split('='))
    # [['3 - 4 ', ' -3'], ['5 + 6 ', ' 11']]
    for i, j in result:
        if eval(i.strip()) == int(j.strip()):
            answer.append('O')
        else:
            answer.append('X')
    # print(result) = [['3 - 4 ', ' -3'], ['5 + 6 ', ' 11']]
    # print(answer) = ['X', 'O']
    
    return answer

# 원영이가 구현
def solution(quiz):
    result = []
    answer = []
    
    for question in quiz:
        # 똑같이 quiz 요소를 = 을 기준으로 나눠줌
        solve, result = question.split('=')
        solve = solve.strip()
        result = int(result.strip())
        
        # 연산자가 없을 경우 그자리에서 break
        operator = None 
        for char in solve:
            if char in ('+', '-'):
                operator = char
                break

        # 연산자가 있을 경우 계산
        if operator:
            num1, num2 = map(int, solve.split(operator))
            cal_result = num1 + num2 if operator == '+' else num1 - num2

            if cal_result == result:
                answer.append('O')
            else:
                answer.append('X')
        else:
            # 연산자가 없을 경우
            if result == int(char):
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