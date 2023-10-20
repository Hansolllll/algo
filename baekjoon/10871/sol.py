import sys
sys.stdin = open('input.txt')

N, X = map(int, input().split())
numbers = list(map(int, input().split()))
# numbers = input()

for num in numbers:
    if num < X:
        print(num, end = " ")

# 런타임에러
# N, X = map(int, input().split())
# numbers = list(map(int, input().split()))

# numbers2 = ''
# for num in numbers:
#     if num < X:
#         numbers2.append(num)
# result = ' '.join(map(str, numbers2))

