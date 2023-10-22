def solution(array, commands):
    
    answer2 = []
    for i in range(len(commands)):
        answer1 = []
        for j in range(len(array)):
            if j >= commands[i][0]-1 and j <= commands[i][1]-1:
                answer1.append(array[j])
                answer1.sort()

        for k in range(len(answer1)):
            if k == commands[i][-1] -1:
                answer2.append(answer1[k])


    return answer2

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))