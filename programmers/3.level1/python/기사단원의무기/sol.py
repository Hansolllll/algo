def solution(number, limit, power):
    answer = []
    # 자연수 1부터 n까지 반복 
    for i in range(1,number+1):
        count = 0
        # i에 루트씌운 값 까지만 반복 
        for k in range(1, int(i**(1/2)) + 1):
            # k가 i의 약수라면 카운트 +1
            if i % k == 0:
                count += 1
                # k가 i의 제곱근이 아니라면 반대되는 약수의 수 +1
                if k ** 2 != i:
                    count += 1
        # 반복문 후에 limit 넘는 수 확인 
        if count > limit:
            count = power
        # count수 answer에 추가
        answer.append(count)

    return sum(answer)

    # 시간초과 
    # count = [0 for num in range(number)]
    # count[0] = 1

    # i = 2
    # while i <= number:
    #     for _ in range(1, round(i**(0.5)+1):
    #         if i % _ == 0:
    #             count[i-1] += 1
    #     i += 1

    # for j in range(len(count)):
    #     if count[j] > limit:
    #         count[j] = power

    # return sum(count)



print(solution(5,3,2))
print(solution(10,3,2))