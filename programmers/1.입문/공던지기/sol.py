def solution(numbers, k):
    num_list = numbers * 50
    count = 0
    for i in range(0,len(num_list), 2):
        count += 1
        if count == k:
            return num_list[i]
 




    # if 2 * (k-1) >= len(numbers):
    #     idx = 2 * (k-1) - len(numbers)
    #     answer = numbers[idx]

print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))