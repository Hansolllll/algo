def solution(n):
    answer = 0

    for num in str(n):
        answer = answer + int(num)

    return answer

def solution(n):
    return sum([int(char) for char in str(n)])

print(solution(1234))
print(solution(930211))