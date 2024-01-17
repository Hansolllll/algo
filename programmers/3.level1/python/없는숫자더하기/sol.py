def solution(numbers):
    num_list = [i for i in range(10)]
    for num in numbers:
        if num in num_list:
            num_list.remove(num)

    return sum(num_list)

def solution(numbers):
    return 45 - sum(numbers)
    
print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))
