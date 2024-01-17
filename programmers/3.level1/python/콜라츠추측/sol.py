def solution(num):
    count = 0
    while num != 1:
        if count >= 500:
            return -1
        else:
            # 홀수라면 
            if num % 2 :
                num = 3*num + 1
                count += 1
            # 짝수라면
            else:
                num /= 2
                count += 1
    return count




    answer = 0
    
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))
