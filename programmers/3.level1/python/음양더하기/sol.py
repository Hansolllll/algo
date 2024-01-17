def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            total += absolutes[i]
        else:
            total -= absolutes[i]
    return total

def solution(absolutes, signs):
    resigns = []
    for i in signs:
        if i == True:
            resigns.append(1)
        else:
            resigns.append(-1)

    answer = sum(map(lambda x, y: x * y, absolutes, resigns))
    return answer
    
print(solution([4, 7, 12], [True,False,True]))
print(solution([1, 2, 3], [False,False,True]))

