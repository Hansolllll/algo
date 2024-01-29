def solution(k, score):
    answer = score[:k]
    low_score = []
    # k이전
    # 점수들 중 가장 낮은 점수를 low_score에 추가
    for _ in range(len(answer)):
        low_score.append(min(answer[:_+1]))
    # k 이후 
    # answer에서 가장 낮은 수와 점수비교해서 더 크면 answer에 추가
    # answer에서 가장 낮은 점수 찾아서 low_scoer에 추가
    for i in range(k, len(score)):
        if score[i] > min(answer):
            answer.remove(min(answer))
            answer.append(score[i])
            low_score.append(min(answer))
        else:
            low_score.append(min(answer))
    return low_score

print(solution(3,[10,100,20,150,1,100,200]))
print(solution(4,[0,300,40,300,20,70,150,50,500,1000]))