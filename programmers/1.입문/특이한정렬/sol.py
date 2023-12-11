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

# lambda이용
def solution(numlist, n):
    # numlist를 sort 후 
    # 딕셔너리 형태로 각 요소와의 차이를 적어서 절대값 처리
    # lambda 함수로 튜플 생성 후 key값 반환
    return sorted(numlist, key = lambda x: (abs(x - n), -x))

# 다른사람의 추가 설명
# key에 요소를 리스트 혹은 튜플로 두 개 이상 줄 수 있다. 
# 이 경우 앞에 값이 같을 때 뒤의 값을 이용해서 나열한다. 
# 요소 하나이고 값이 같을 때는 먼저 처리된 수가 먼저 나열되는 것 같다(인덱스가 작은 것이).

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))
