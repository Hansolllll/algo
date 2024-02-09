def solution(answers):
    # 길이가 10000인 리스트 만들기 
    man1 = [1,2,3,4,5] * 2000
    man2 = [2,1,2,3,2,4,2,5] * 1250
    man3 = [3,3,1,1,2,2,4,4,5,5] * 1000

    # 학생별 맞힌 개수 딕셔너리 만들기
    score = {1:0, 2:0, 3:0}

    # 반복문으로 학생당 맞힌 개수 추가
    for i in range(len(answers)):
        if man1[i] == answers[i]:
            score[1] += 1
        if man2[i] == answers[i]:
            score[2] += 1
        if man3[i] == answers[i]:
            score[3] += 1
    # 딕셔너리에서 밸류 기준 내림차순 정렬
    array = sorted(score.items(), key = lambda item:item[1], reverse=True)

    # 정렬시 1등학생이랑 2등학생의 맞힌 개수가 다르다면 1등만 출력
    if array[0][1] != array[1][1]:
        return [array[0][0]]
    
    # 최고점 학생이 2명인 경우 2명 출력
    elif array[1][1] != array[2][1]:
        return [array[0][0], array[1][0]]
    
    # 3명이 같은 점수일 경우 3명다 출력 
    else:
        return [array[0][0], array[1][0], array[2][0]]

        
    
  

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))