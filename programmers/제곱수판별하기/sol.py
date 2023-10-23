def solution(n):
    a = int(n ** (1/2))
    if n == a**2:
        return 1
    else:
        return 2


print(solution(144))
print(solution(976))