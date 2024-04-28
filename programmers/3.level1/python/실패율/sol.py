# def solution(N, stages):
#     answer = []
#     # 0으로 채워진 리스트 만들기(인덱스가 단계 의미)
#     val = [0 for i in range(1, N+1)]

#     # 단계에 있는 사람 수 count 
#     for k in range(1, N+1):
#         count = 0
#         user = 0
#         for num in stages:
#             # 클리어하지 못한 사람(분자)
#             if num == k:
#                 count += 1 
#             # 도전한 사람(분모)
#             if num >= k:
#                 user += 1
#         # 실패율 계산해서 val에 넣기
#         val[k-1] = count / user

#     # answer의 길이가 N이 될 때까지 반복
#     while len(answer) < N:
#         # 가장 큰 수의 인덱스 +1 (실패율이 가장 큰 레벨)을 answer에 추가
#         answer.append(val.index(max(val))+1)
#         # 추가한 후에는 비교에 방해되지 않게 음수로 바꿔놓기 
#         val[val.index(max(val))] = -1

#     return answer
        
def solution(N, stages):
    answer = []
    # val = []

    val = [0] * N
    for num in stages:
        if num <= N:
            val[num - 1] += 1

    # for i in range(N):
    #     count = 0
    #     for num in sorted(stages):
    #         if num == i+1:
    #             count += 1
    #         if num > i+1:
    #             break
    #     val.append(count)

    for k in range(N):
        try:
            answer.append(val[k]/(len(stages)-sum(val[:k])))
        except:
            answer.append(0)

    answer2 = []
    for m in range(N):
        idx = answer.index(max(answer))
        answer2.append(idx+1)
        answer[idx] = -1


    return answer2
print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))