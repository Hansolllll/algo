from itertools import combinations

def solution(numbers):
    answer = []
    # numbers에서 두 숫자 뽑아서 
    for x,y in combinations(numbers, 2):
        # 두 수의 합이 answer에 없다면 추가 
        if x+y not in answer:
            answer.append(x+y)
    # 정렬해서 return
    return sorted(answer)

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))