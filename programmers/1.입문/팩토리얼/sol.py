def solution(n):
    i = 1
    total = 1 
    while total <= n:
        i += 1
        total = i * total
    return i - 1

# math 내장함수 이용
import math
# result ! 값이 n값보다 클때 멈춘다.
def solution(n):
    i = 1
    while math.factorial(i) <= n:
        i +=1
    return i-1

# 반복문으로 순차적으로 나누기
def solution(n):
    i = 1   # 0부터 나누면 안되니까 1부터 시작
    while n//i > 0:
        n //= i   # //: 몫
        i += 1    # i 1씩 증가 해서 나누기 1, 나누기 2, 나누기 3...
    return i-1


print(solution(3628800))
print(solution(7))
