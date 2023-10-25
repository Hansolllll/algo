def solution(box, n):
    # 반복문으로 가로/세로/높이 수용가능한 큐브 수 누적 곱하기
    answer = 1
    for i in range(len(box)):
        answer *= (box[i] // n)

    return answer

print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))