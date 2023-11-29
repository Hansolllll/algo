def solution(x):
    result = 0
    for char in str(x):
        result += int(char)
    if x % result == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
