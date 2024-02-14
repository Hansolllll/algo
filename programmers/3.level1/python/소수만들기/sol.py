from itertools import combinations

def solution(nums):
    answer = 0
    # nums에서 3개 뽑아 그 합을 num에 지정
    for x,y,z in list(combinations(nums, 3)):
        num = x+y+z
        count = 0
        # num의 제곱근까지만 반복 
        for _ in range(1, int(num**(1/2))+1):
            if num % _ == 0:
                count += 1
                if (_**2) != num:
                    count += 1
        
        # num의 약수가 2개라면 answer 갯수 +1
        if  count == 2:
            answer += 1

    return answer
                

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))