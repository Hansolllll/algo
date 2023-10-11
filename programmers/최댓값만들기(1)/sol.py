def solution(numbers):
    num_list = sorted(numbers)
    answer = num_list[-1] * num_list[-2]

    return answer

def solution(numbers):
    answer = 0

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            multi = numbers[i] * numbers[j]

            if answer < multi:
                answer = multi

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))