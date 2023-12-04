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

# 하이브리드 소트 ?
def solution(scores):
    answer = []
    
    for i, score in enumerate(scores, start=1): #각 학생에게 1번부터 번호표 부착
        avg_score = sum(score) / len(score) #각 학생의 평균 계산(len(score)대신 2를 넣어도 됨.)
        
        rv_student = 0 # rv = Reference value(등수)

        for student in scores:
            rv_score = sum(student) / len(student) # 전체 평균을 구해서 rv_score 작성

            if rv_score > avg_score: # 학생 score가 평균보다 작으면
                rv_student += 1 # 등수를 하나 올려준다.(1등보다2등이 낮은 거임, 숫자가 올라갈수록 낮은 등수)

        answer.append(rv_student + 1)

    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
