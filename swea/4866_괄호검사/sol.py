import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = input() # input data 받아오기 
    stack = [] # stack 이라는 빈 list 만들기
 
    for char in string:
        # 열리는 괄호만 일단 stack에 넣기
        if char == '{' or char == '(': 
            stack.append(char)

        # 닫히는 괄호일 경우 (소괄호 중괄호 동일)
        elif char == '}': 
            # stack에 데이터가 있고, stack의 맨마지막 데이터가 괄호와 대응되는지 확인 
            if len(stack) and stack[-1] == '{': 
                stack.pop() # 확인후에 pop
            else: 
                stack.append(char)

        elif char == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else: 
                stack.append(char)

    # 괄호가 다 서로 대응되어 stack에 아무것도 없다면 1 아니면 0
    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
