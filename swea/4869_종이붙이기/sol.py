import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    N = int(input()) // 10

    memo = [0, 1, 3]

    while N >= len(memo):
        result = memo[len(memo)-2] * 2 + memo[len(memo)-1]
        memo.append(result)

    print(memo[N])