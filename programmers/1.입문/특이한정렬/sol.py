def solution(numlist, n):
    answer = []
    
    # numlist에 하나도 안남을때 까지 for문 반복
    while len(numlist) != 0:
        # val은 충분히 큰 숫자
        val = 100000    

        # n과의 거리 비교해서 더 작은 값을 val에 넣기
        for num in numlist:
            if abs(num-n) < abs(val-n):
                val = num

            # 만약 거리가 같다면 더 큰 수를 val에 넣기
            elif abs(num-n) == abs(val-n):
                val = max(val, num)

        # val을 answer에 넣고, numlist에서 제거하기
        answer.append(val)
        numlist.remove(val)

    return answer



print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))
