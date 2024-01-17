def solution(n):
    n = str(n)
    answer = []
    for i in range(len(n)):
        answer.insert(0, int(n[i]))

    return answer

print(solution(12345))
