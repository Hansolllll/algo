def solution(n):
    # 1 ~ n 까지의 수 포함하는 리스트 만들기
    answer = []
    num_list = [num for num in range(1, n+1)]

    # 리스트 내에서 반복문 돌려서 n이 num으로 나눠지는지 확인 후 리스트에 추가
    for num in num_list:
        if n % num == 0:
            answer.append(num)

    return answer


print(solution(24))
print(solution(29))