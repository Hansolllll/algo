from itertools import combinations

def solution(number):
    answer = 0
    # 조합들 내에서 반복문을 돌려 합이 0이되면 answer+1 
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1

    return answer
print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))