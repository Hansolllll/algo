import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    numbers = list(map(int, input().split()))

    max_num = 0
    min_num = 100000000
    idx = 0
    
    while idx < len(numbers):
        if numbers[idx] > max_num:
            max_num = numbers[idx]

        if numbers[idx] < min_num:
            min_num = numbers[idx]        
        idx += 1

    result = max_num - min_num

    print(f'#{tc} {result}')

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
    
#     numbers = list(map(int, input().split()))

#     min_num = 1000000
#     max_num = 0

#     for num in numbers:
#         if min_num > num:
#             min_num = num
        
#         if max_num < num:
#             max_num = num
    
#     result = max_num - min_num
#     print(f'#{tc} {result}')