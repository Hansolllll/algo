def solution(score):
    # score 안의 값을 평균으로 바꿔 넣기
    for i in range(len(score)):
        score[i] = sum(score[i])/len(score[i])
    
    # sort된 리스트(rank)와 score의 값을 비교
    # => rank에서 score의 인덱스를 순위로 이용 
    rank = sorted(score, reverse=True)

    for j in range(len(score)):
        score[j] = rank.index(score[j]) + 1

    return score

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
