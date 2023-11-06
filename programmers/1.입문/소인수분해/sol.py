def solution(n):
    answer = []

    for i in range(2, n+1):
        while n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i
    return answer


def solution(n):
    answer = [] 
    
    while n % 2 == 0:      # 짝수라면  // 홀수라면
        answer.append(2)   # answer리스트에 2를 일단 append한다 
        n //= 2            # 계속 2로 나눠준다 가장작은 홀수가 나올때까지
  
    for i in range(3, n + 1, 2):     
        #홀수라면 for문으로 들어온다(1,2는 계산할필요가 없으니까 3부터시작, +2를 해주며 홀수로만)
        while n % i == 0:   # n이 홀수로 나누어 떨어지면
            answer.append(i) # 홀수 i를 answer리스트에 append
            n //= i          
    
    answer = list(set(answer)) # 중복제거
    return sorted(answer)   #안했더니 통과 못하는 케이스 존재
print(solution(10000))

# answer = []

#     for i in range(1, n):
#         if n % i == 0:
#             answer.append(n//i)
#             answer.sort()


#     return answer

print(solution(12))
print(solution(17))
print(solution(420))