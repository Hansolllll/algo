from itertools import combinations
def solution(dots):
    coef = []
    # 두개 뽑아서 기울기 구한다음 coef에 넣기
    for [x1, y1], [x2, y2] in combinations(dots, 2):
        coef.append((x2-x1)/(y2-y1))
        
    # coef 절반까지만 반복문 돌려서 양끝에 대치대는 위치의 기울기가 같은지 확인
    for i in range(len(coef)//2):
        if coef[i] == coef[len(coef)-i-1]:
            return 1
    else:
        return 0 


# 접근이 잘못됨, 두개가 뽑히면 나머지 두개와의 기울기 비교 해야함
# 근데 5, 14 빼고 전부 통과 ...?
# def solution(dots):
#     coef = []
#     for [x1, y1], [x2, y2] in combinations(dots, 2):
#         coef.append((x2-x1)/(y2-y1))

#     for _ in coef:
#         if coef.count(_) >= 2:
#             return 1
#     return 0


# print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
# print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
print(solution([[1, 5], [2, 4], [3, 9], [4, 8]])) # 1
print(solution([[1,2], [2,1], [3,4], [4,5]])) # 0
print(solution([[1, 1], [10, 8], [7, 7], [8, 6]])) # 1