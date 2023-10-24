def solution(array):
    # 반복문으로 배열 내 가장 큰 값 찾은 후 리턴
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return [max, array.index(max)]


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))

