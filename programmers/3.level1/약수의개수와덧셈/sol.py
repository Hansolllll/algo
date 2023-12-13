def solution(left, right):
    answer = 0
    # left에서 right까지 반복
    for num in range(left, right+1):
        count = 0
        # num의 약수 갯수 구하기 
        for _ in range(1,num+1):
            if num % _ == 0:
                count += 1
        # 약수 갯수가 홀수라면
        if count % 2:
            answer -= num
        # 약수 갯수가 짝수라면
        else:
            answer += num

    return answer
    
print(solution(13, 17))
print(solution(24, 27))