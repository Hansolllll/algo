def solution(array):
    array = map(str, array)
    total = 0
    for num in array:
        total += num.count('7')
    
    return total


print(solution([7,77,17]))
print(solution([10, 29]))