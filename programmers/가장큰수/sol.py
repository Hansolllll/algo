def solution(numbers):
    numbers = list(map(str, numbers))
    max_num = 0
    answer = ''
    # answer = 
    # for i in range(len(numbers)):
    for num in numbers:
        if int(num[0]) > int(max_num):
            max_num = num 

    answer += max_num




 
            


    print(answer)
    # for num in numbers:

    # answer = ''
    # return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))




