def solution(box, n):
    di_box = box[0] * box[1]
    di_cube = n ** 2

    a = box[0] // n * 2
    b = box[1] // n * 2
    height = box[2] // n
    result = di_box // di_cube * height

    return result


print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))