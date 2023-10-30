def solution(my_string):
    stack = []
    for char in my_string:
        # 스택에 아무것도 없다면 추가
        if len(stack) == 0:
            stack.append(char)
        # 스택 안에 문자 있다면 비교
        else:
            # 문자가 스택에 없을 때만 추가
            if char not in stack:
                stack.append(char)
            
    # 문자열로 변환해서 리턴
    return ''.join(stack)

# 내장함수 사용
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

print(solution('people'))
print(solution('We are the world'))