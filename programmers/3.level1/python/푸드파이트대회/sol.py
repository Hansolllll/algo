def solution(food):
    answer = ''
    idx = 0
    for num in food[1:]:
        idx += 1
        answer += str(idx) * (num // 2)

    return answer+'0'+answer[::-1]


print(solution([1,3,4,6]))
print(solution([1,7,1,2]))