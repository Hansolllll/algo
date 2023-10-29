def solution(array, n):
    answer = 100
    for num in array:
        if abs(num - n) < abs(answer - n):
            answer = num
        elif abs(num - n) == abs(answer - n):
            answer = min(num, answer)
    return answer

print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))