def solution(n):
    answer = []
    num_list = [num for num in range(1, n+1)]

    for num in num_list:
        if n % num == 0:
            answer.append(num)

    return answer


print(solution(24))
print(solution(29))