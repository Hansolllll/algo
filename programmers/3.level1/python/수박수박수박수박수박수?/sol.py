def solution(n):
    answer = ''
    
    while len(answer) < n:
        if len(answer) % 2 :
            answer += '박'
        else:
            answer += '수' 
    
    return answer

print(solution(3))
print(solution(4))