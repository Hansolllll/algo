def solution(s):
    # s 안에 1개만 있는 문자만 stack에 추가
    stack = []
    for char in s:
        if s.count(char) == 1:
            stack.append(char)

        stack.sort() # 문자 순서대로 정렬
        return ''.join(stack) # 문자열로 출력 

    # 짧은버전
    stack = [char for char in s if s.count(char) == 1]
    stack.sort()
    return ''.join(stack)


print(solution('abcabcadc'))
print(solution('abdc'))
print(solution('hello'))