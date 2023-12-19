def solution(num, total):
    # total 범위 잡기
    for i in range(-100, total):
        answer = []
        # 1개 숫자인 경우엔 바로 total return하기
        if num == 1:
            return [total]
        # 여러개의 숫자 필요한 경우 answer 리스트에 넣고 그 합을 비교하기
        else:
            for j in range(num):
                answer.append(i+j)
            if sum(answer) == total:
                return answer
         
print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))