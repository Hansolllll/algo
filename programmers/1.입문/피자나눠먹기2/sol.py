def solution(n):
    numlist = [num for num in range(1, n+1)]
    # n과 6의 최소공배수 찾기
    for num in numlist:
        if (6*num) % 6 == 0 and (6*num) % n == 0:
            return num
            break

# math 함수 호출(3.9부터 지원하여 프로그래머스에선 실행 불가)
# GCD함수(greatest common divisor) : 최대공약수를 찾는 함수, 유클리드알고리즘 관련 
# 유클리드 호제법 관련 문서 : https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95

# math 함수 호출
import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6


print(solution(6))
print(solution(10))
print(solution(4))