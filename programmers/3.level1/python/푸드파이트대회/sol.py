def solution(food):
    # 풀이 1 
    answer = ''
    # food.index(num)으로 할 경우 동일한 숫자가 2개 이상 있을 시 
    # 인덱스가 제대로 반환되지 않음 
    idx = 0
    # food에서 1번 음식부터 반복
    for num in food[1:]:
        idx += 1
        # 음식 번호를 (음식갯수/2)의 몫만큼만 반복 
        answer += str(idx) * (num // 2)
    # 왼쪽부터 먹는 배치 + 물 + 오른쪽부터 먹는 배치  
    return answer+'0'+answer[::-1]

    # 풀이 2 
    # 리스트 컴프리헨션 
    return ''.join([str(i)*(food[i]//2) for i in range(1, len(food))]  + ['0'] +  [str(i)*(food[i]//2) for i in range(1, len(food))][::-1])

print(solution([1,3,4,6]))
print(solution([1,7,1,2]))