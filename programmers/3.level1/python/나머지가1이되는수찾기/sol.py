def solution(n):
    # 컴프리헨션
    return [i for i in range(1, n+1) if n % i == 1][0]
    
    # 기본 풀이
    for i in range(1, n+1):
        if n % i == 1:
            return i


print(solution(10))
print(solution(12))