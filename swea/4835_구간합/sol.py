import sys
sys.stdin = open('input.txt')

T = int(input())

# 풀이 2
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 10000000000

    for i in range(N-M+1):
        # num_list에 numbers의 시작점부터 M개의 숫자 할당
        num_list = numbers[i:i+M]
        # 그 때 num_list의 합을 max_sum, min_sum과 비교하기
        if sum(num_list) > max_sum:
            max_sum = sum(num_list)
        if sum(num_list) < min_sum:
            min_sum = sum(num_list)
            
    print(f'#{tc} {max_sum - min_sum}')

# 풀이 1
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))

#     max_sum = 0
#     min_sum = 1000000000000000
#      # 구간합을 구하기 위한 i(시작점) => 뒤에 M개의 데이터를 더하기 위한 시작점
#     for i in range(N-M+1):
#         total = 0

#         # 시작점을 기준을 오른쪽 M개의 숫자합
#         for j in range(M):
#             total = total + numbers[i+j]
#         # total += numbers[i+j]

#         if total > max_sum:
#             max_sum = total
#         if total < min_sum:
#             min_sum = total
#     result = max_sum - min_sum

#     print(f'#{tc} {result}')
