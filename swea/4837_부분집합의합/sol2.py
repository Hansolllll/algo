import sys
from itertools import combinations
sys.stdin = open('input.txt')


T = int(input())
A = [i for i in range(1, 13)]

for tc in range(1, T+1):
    # N : 부분집합 원소 수 , K: 부분집합의 합
    N, K = map(int, input().split()) 
    numbers = list(combinations(A, N))

    count  = 0
    for num in numbers:
        if sum(num) == K:
            count += 1

    print(f'#{tc} {count}')