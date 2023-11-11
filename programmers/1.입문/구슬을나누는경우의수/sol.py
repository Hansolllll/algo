from math import comb
# combination함수 => 이터레이터를 반환 (리스트함수로 명시해야함)
# comb함수 => 조합의 개수를 직접 반환
def solution(balls, share):
    return comb(balls, share)

# 테스트케이스 5,6,7,35 
#=> 리스트 만들고 share 개수대로 뽑아서 다시 리스트 만드는 방식은 메모리소요가 큼
# from itertools import combinations

# def solution(balls, share):
#     balls_list = [i for i in range(balls)]
#     return len(list(combinations(balls_list, share)))



print(solution(3, 2))
print(solution(5, 3))