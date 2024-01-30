def solution(cards1, cards2, goal):
    # goal에 문자가 있다면 반복 
    while len(goal) >= 1:
        # card1과 2의 길이 조건을 넣지 않으면 인덱스 오류 발생
        # card1과 goal의 0번 원소가 같다면 각각 제거 
        if len(cards1) > 0 and goal[0] == cards1[0]:
            goal.pop(0)
            cards1.pop(0)
        # card2와 goal의 0번 원소가 같다면 각각 제거 
        elif len(cards2) > 0 and goal[0] == cards2[0]:
            goal.pop(0)
            cards2.pop(0)
        # goal의 0번 원소가 card1, card2의 0번 원소와 다르다면 'No'
        #(순서 다를 경우)
        else:
            return 'No'
    
    return 'Yes'

    # # 런타임 에러 
    # for i in range(len(goal)):
    #     if goal[i] in cards1:
    #         cards1[cards1.index(goal[i])] = i
    #     elif goal[i] in cards2:
    #         cards2[cards2.index(goal[i])] = i
    #     else:
    #         return 'No'
    # if cards1 != sorted(cards1) or cards2 != sorted(cards2):
    #     return 'No'

    # return 'Yes'

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))