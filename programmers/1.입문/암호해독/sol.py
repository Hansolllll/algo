def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
        if (i+1) % code == 0:
            answer += cipher[i]
    return answer


print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))