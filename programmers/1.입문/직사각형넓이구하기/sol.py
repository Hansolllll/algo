def solution(dots):
    for i in range(len(dots)-1):
        if dots[i][0] != dots[i+1][0]:
            x = dots[i][0] - dots[i+1][0]
        if dots[i][1] != dots[i+1][1]:
            y = dots[i][1] - dots[i+1][1]

    return abs(x * y)

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))