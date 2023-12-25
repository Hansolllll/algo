def solution(n):
    answer = []
    n = int(n)
    while  n > 0:
        answer.append(n%3)
        n = n // 3
    return(int(''.join(map(str,answer)), 3))

    

print(solution(45))
print(solution(125))
