import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) 
    # N : 부분집합 원소 수 , K: 부분집합의 합
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(A)
    
    result = []
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(A[j])
        if len(temp) == N and sum(temp) == K:
            result.append(temp)
    print(f'#{tc} {len(result)}')







# n = len(numbers)

# for i in range(1<<n):
# # for i in range(2**n):와 동일 
#     # print(i)

#     temp = []
#     for j in range(n):
#         # print(i, bin(i), bin(1<<j))
#         if i & (1<<j):
#             temp.append(numbers[j])
#     print(temp)