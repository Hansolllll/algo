import sys
sys.stdin = open('input.txt')

T = 10 

for tc in range(1, T+1):
    tc = int(input())
    matrix = []

    # i, j, a 반복문 돌리는 변수 지정
    # _ = 변수를 활용하지 않을 예정
    for _ in range(100):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    max_total = 0

    # 가로줄
    for row in range(len(matrix)):
        total = 0    
        for col in range(len(matrix[0])):
            total += matrix[row][col]

        if max_total < total:
            max_total = total
    # 세로줄
    for col in range(100):
        total = 0
        for row in range(100):
            total += matrix[row][col]
        if max_total < total:
            max_total = total

    # 대각선(좌 -> 우)
    total = 0
    for i in range(100):
        total += matrix[i][i]

    if max_total < total:
        max_total = total

    # 대각선(우 -> 좌)
    total  = 0
    for i in range(100):
        total += matrix[i][99-i]
    
    if max_total < total:
        max_total = total

    print(max_total)

