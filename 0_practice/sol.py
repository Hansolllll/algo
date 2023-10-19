import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
 
    for char in string:
        if char == '{' or char == '(':
            stack.append(char)
        elif char == '}':
            if len(stack) and stack[-1] == '{':
                stack.pop()
            else: 
                stack.append(char)
        elif char == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else: 
                stack.append(char)

    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
