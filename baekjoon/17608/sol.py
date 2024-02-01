import sys
sys.stdin = open('input.txt')

TC = int(input())
blocks = []

for i in range(TC):
    num = int(input())
    blocks.append(num)

count = 1
for j in blocks[::-1]:
    std = blocks[-1]
    if j > std:
        count += 1
        std = j

print(count)
