def solution(s):
    num_list = list(s.split())
    
    stack = []
    for num in num_list:
        # num_list에서 Z가 아닐경우 stack에 추가
        if num != 'Z':
            stack.append(num)
        # Z일 경우 그 앞의 숫자 stack에서 꺼내기
        else:
            stack.pop()

    stack = map(int, stack)
    return sum(stack)

print(solution('1 2 Z 3'))
print(solution('10 20 30 40'))
print(solution('10 Z 20 Z 1'))
print(solution('10 Z 20 Z'))
print(solution('-1 -2 -3 Z'))