def solution(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        return numbers[0] * numbers[1]
    else:
        return numbers[-1] * numbers[-2]
   
   
    # max1 = -10000
    # max2 = -10000
    # for num in numbers:
    #     if num > max1:
    #         max1 = num
    # for num in numbers:
    #     if num > max2 and num < max1:
    #         max2 = num

    # answer = max1 * max2
    # return answer

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))

