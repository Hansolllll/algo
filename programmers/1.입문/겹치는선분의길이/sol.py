def solution(lines):
    numbers = []
    # 시작점을 기준으로 길이가 1인 선분을 튜플형태로 만들어서 numbers에 추가
    for i in range(len(lines)):
        for num in range(lines[i][0], lines[i][-1]):
            numbers.append((num, num+1))
    
    scope= []
    # numbers안에서 2번 이상 중복되는 선분 중 한번만 scope에 추가하기
    for _ in numbers:
        if numbers.count(_) >= 2 and _ not in scope:
            scope.append(_)

    # scope의 원소갯수 return
    return len(scope)

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))