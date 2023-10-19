import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    width = int(input())  # 주어진 직사각형 가로 크기
    height = 20 # 고정된 세로 크기 
    dimension = 20 * int(input())

    # 직사각형 종이(width * height, dimension) 
    # 10*20,200 / 20*20,400
    di1 = 200
    di2 = 400

    dp = [0]*100
    dp[0] = 0

    for num in dp:
