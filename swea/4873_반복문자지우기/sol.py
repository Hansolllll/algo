import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    string = input()
    stack = []

    for char in string:
        #스택 빈 경우
        if len(stack) == 0:
            stack.append(char)

        # 스택 차있는 경우
        else: 
            # 스택 마지막 데이터와 비교 데이터가 같은 경우
            if char == stack[-1]:
                stack.pop()
            # 같지 않은 경우
            else:
                stack.append(char)
    
    print(len(stack))



    
