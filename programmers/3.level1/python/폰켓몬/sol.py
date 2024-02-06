from itertools import permutations
# 문제파악 다시 하기 
# permutation을 쓸 이유가 없음 
def solution(nums):
    # 골라야하는 폰켓몬의 수가 폰켓몬 종류보다 많다면 폰켓몬 종류 수 만큼 리턴
    if len(nums)//2 >= len(set(nums)):
        return len(set(nums))
    # 고를 폰켓몬 수 보다 주어진 종류가 더 많다면 고를 마리 수만큼 리턴
    else:
        return len(nums)//2

# 시간초과 2
# def solution(nums):
#     return max(list(map(len,(map(set,permutations(nums, len(nums)//2))))))

# 시간초과 1
# def solution(nums):
#     pick = list(permutations(nums, len(nums)//2))
#     for i in range(len(pick)):
#         pick[i] = len(set(pick[i]))
#     return max(pick)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))