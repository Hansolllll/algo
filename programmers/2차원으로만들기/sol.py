def solution(num_list, n):
    groups = len(num_list) // n


    # answer = [[] for _ in range(groups)]
    # for num in num_list:
    #     for i in range(len(answer)):
    #         if len(answer[i]) <= n-1:
    #             answer[i].append(num)
    #         else:
                

    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))