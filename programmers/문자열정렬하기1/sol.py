def solution(my_string):
    answer = []
    for char in my_string:
        try:
            answer.append(int(char))
        except:
            continue
    answer.sort()
    return answer

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))