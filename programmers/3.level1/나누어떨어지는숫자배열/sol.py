def solution(arr, divisor):
    answer = []
    for num in arr:
        # 나눠떨어지지 않는다면
        if num % divisor == 0:
            answer.append(num)
    if len(answer) == 0:
        return [-1] 
    else:
        return sorted(answer)

print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3,2,6], 10))
