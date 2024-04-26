def solution(n):
    a = int(n ** (1/2))
    if n == a**2:
        return 1
    else:
        return 2

def solution(n):
    return 1 if n**0.5 == round(n**0.5) else 2

print(solution(144))
print(solution(976))