def solution(numbers):
    answer = 0
    sum = 0

    for number in numbers:
        sum = sum + number
        
    answer = sum / len(numbers)
    return answer

#  def solution(numbers):
#     return sum(numbers) / len(numbers)


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))


