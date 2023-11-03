def solution(before, after):
    # before에 있는 문자열이 after에 있다면 
    for char in before:
        if char in after:
            # replace 이용해서 1개만 '0'으로 바꾸기
            before = before.replace(char, '0', 1)
            after = after.replace(char, '0', 1)

    # 반복문 종료 후 before와 after가 서로 같다면 문자열 내부 문자 갯수가 동일하단 의미
    if before == after:
        return 1
    else:
        return 0

# 정렬 이용해서 풀이
def solution(before, after):
    sort_bef = sorted(before)
    sort_aft = sorted(after)
    if sort_bef == sort_aft:
        return 1
    else:
        return 0
print(solution("olleh","hello"))

print(solution('olleh', 'hello'))
print(solution('allpe', 'apple'))