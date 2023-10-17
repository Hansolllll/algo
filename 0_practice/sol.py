import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    left = 1
    right = P 
    A_count = 0
    while True:
        center = int((left+right)/2)

        if A < center:
            right = center
        elif A > center:
            left = center 
        else:
            break
        A_count += 1

    left = 1
    right = P
    B_count = 0
    while True:
        center = int((left+right)/2)

        if B < center:
            right = center
        elif center < B:
            left = center
        else:
            break
        B_count += 1 
    
    winner = 0
    if A_count < B_count:
        winner = "A"
    elif B_count < A_count:
        winner = "B"
    
    print(f'#{tc} {winner}')
        