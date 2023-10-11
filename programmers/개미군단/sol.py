# 장군개미 = 5 = num1
# 병정개미 = 3 = num2
# 일개미 = 1 = num3

def solution(hp):
    num1 = hp // 5 
    num2 = (hp % 5) // 3
    num3 = (hp % 5) % 3    
    
    answer = num1 + num2 + num3

    return answer

def solution(hp):
    answer = 0

    a, b = divmod(hp, 5)
    hp = b
    answer += a

    a, b = divmod(hp, 3)
    hp = b 
    answer += a

    answer += hp

    return answer

print(solution(23))
print(solution(24))
print(solution(999))