def solution(a, b, n):
    # 상빈이가 받을 수 있는 콜라의 수 : answer 
    answer = 0

    # 가지고 있는 콜라수가 a개 이상이면 반복 
    while n >= a:
        # 몇 묶음인지 변수에 저장 
        bundle = n // a 
        # 콜라 총 갯수에서 마트에 주는 만큼 빼고
        # 마트에서 받는만큼 콜라 수에 더하기
        n -= bundle * a
        n += bundle * b

        # 총 콜라수 말고 마트에서 받은 수만 따로 카운트
        answer += bundle * b
    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))
