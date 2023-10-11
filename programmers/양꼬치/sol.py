def solution(n, k):
    service = 0

    if n >= 10:
        service = n // 10
        k = k - service

    sum_n = 12000 * n 
    sum_k = 2000 * k 
    answer = sum_n + sum_k
    
    return answer



print(solution(10, 3))
print(solution(64, 6))