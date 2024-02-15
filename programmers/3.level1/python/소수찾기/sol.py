def solution(n):
    answer = 0
    # 2부터 소수판별
    for i in range(2, n+1):
        # i의 제곱근까지만 반복 
        # 소수는 1과 본인만 가지므로 이외 약수 있으면 break
        for k in range(2, int(i**0.5)+1):
            if i % k == 0:
                break
        # break만나지 않고 끝나면 answer +1 
        else:
            answer += 1
    return answer
        

    # 시간초과 
    # answer = 0
    # for i in range(2, n+1):
    #     count = 1
    #     for k in range(2, int(i**0.5)+1):
    #         if i % k == 0:
    #             count += 1
            
    #     if count == 1:
    #         answer += 1 

    # return answer

print(solution(10))
print(solution(5))