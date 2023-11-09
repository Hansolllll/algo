def solution(sides):
    sides.sort()
    num = []
    # 경우 1 => sides안 숫자가 가장 큰수일 때
    for i in range(1, sides[-1]+1):
        if i + sides[0] > sides[-1]:
            num.append(i)
    
    # 경우 2 => sides안 숫자가 작은 숫자들일 때
    for j in range(sides[-1], sum(sides)):
        if j <= sum(sides):
            num.append(j)

    return len(set(num))

print(solution([1,2]))
print(solution([3,6]))