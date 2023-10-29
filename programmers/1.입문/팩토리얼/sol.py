def solution(n):
    i = 1
    total = 1 
    while total <= n:
        i += 1
        total = i * total
    return i - 1


print(solution(3628800))
print(solution(7))
