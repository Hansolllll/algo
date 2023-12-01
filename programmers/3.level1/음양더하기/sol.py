def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            total += absolutes[i]
        else:
            total -= absolutes[i]
    return total

print(solution([4, 7, 12], [True,False,True]))
print(solution([1, 2, 3], [False,False,True]))

