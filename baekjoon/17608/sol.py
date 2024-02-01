import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
    
TC = int(input())
blocks = []

for i in range(TC):
    blocks.append(int(input()))

count = 1
std = blocks[-1]
for j in blocks[::-1]:
    if j > std:
        count += 1
        std = j

print(count)
