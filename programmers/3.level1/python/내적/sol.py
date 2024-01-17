def solution(a, b):
    answer = 0
    for i in range(len(a)):
        prod = a[i]*b[i]
        answer += prod
    return answer

    # 고쳐보자
    for i in range(len(a)):
        what = list(map(int, lambda i : a[i]*b[i]))
    return what

def solution(a, b):
    answer = sum(list(map(lambda x, y: x * y, a, b)))
    return answer

print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))