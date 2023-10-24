def solution(my_string):
    # 반복문으로 문자를 정수화해서 정답리스트에 넣기
    # try문으로 문자일 때 발생하는 오류 방지
    answer = []
    for char in my_string:
        try:
            answer.append(int(char))
        except:
            continue
    # 리스트 정렬
    answer.sort()
    return answer

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))