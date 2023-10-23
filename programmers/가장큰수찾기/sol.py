def solution(array):
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return [max, array.index(max)]


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))

