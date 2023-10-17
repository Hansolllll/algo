import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
# P : 전체쪽수 A: a가 찾을 쪽번호 B: b가 찾을 쪽번호
    left = 1
    right = P
    A_count = 0
    while True:
        center = int((left+right)/2)

        # A의 목적페이지가 가운데보다 왼쪽에 있는 경우 
        if  A < center:
            right = center

        # A의 목적페이지가 가운데보다 오른쪽에 있는 경우
        elif center < A:
            left = center

        # A의 목적 페이지에 도달한 경우 
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

    print(A_count, B_count)
