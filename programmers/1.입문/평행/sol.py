from itertools import combinations 

def solution(dots):
    y = []
    for num in dots:
        y.append(num[-1])

    number1 = list(combinations(y, 2))
    number2 = [num for num in y if num not in number1]

    # answer = 0
    return number1, number2

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))