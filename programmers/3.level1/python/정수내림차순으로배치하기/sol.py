def solution(n):
    # 방법1(while문 이용)
    answer = []
    for char in str(n):
        answer.append(char)
    
    result = ''
    while len(answer)!=0:
        result += max(answer)
        answer.remove(max(answer))

    return int(result)

    # 방법2(sort 이용)
    answer = []
    for char in str(n):
        answer.append(int(char))
    answer.sort(reverse=True)
    return int(''.join(map(str,answer)))


print(solution(118372))