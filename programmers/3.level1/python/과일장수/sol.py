def solution(k, m, score):
    answer = 0
    # 역순으로 정렬
    score = sorted(score, reverse=True)
    
    # 시작점 0
    start = 0
    # 시작점부터 시작점+m의 길이가 m 이상일때만 반복
    while len(score[start:start+m]) >= m:
        # 구간에서 가장 작은 점수 * m 개를 더하기
        answer += score[start:start+m][-1] * m
        # 시작점 옮기기
        start += m
    return answer


    # 시간초과
    # while len(score) >= m:
    #     try:
    #         answer += score[0:m][-1] * m
    #         score = score[m:]
    #     except:
    #         return answer
    # return answer


print(solution(3,4,	[1, 2, 3, 1, 2, 3, 1]))
print(solution(4,3,	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))