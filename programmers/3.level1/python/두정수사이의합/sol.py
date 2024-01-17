def solution(a, b):
    num_list = []
    for num in range(min(a,b), max(a,b)+1):
        num_list.append(num)
    return sum(num_list)

    
print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
