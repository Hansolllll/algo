def solution(d, budget):
    d.sort()
    total = 0
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            break
    if total > budget:
        i -= 1
    return i+1
    


# 런타임에러
# def solution(d, budget):
#     answer = 0
#     while budget > min(d):
#         budget -= min(d)
#         d.remove(min(d))
#         answer += 1
        
#     if budget == min(d):
#         answer += 1

#     return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))