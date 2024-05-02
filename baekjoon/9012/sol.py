import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    stack = []
    line = input()
    for char in line:
        if len(stack):
            if char == ')':
                stack.pop()
            else :
                stack.append(char)
        else:
            stack.append(char)  
    
    if len(stack):
        print('NO')
    else:
        print('YES')