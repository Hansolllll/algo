def solution(my_string):
    my_string = my_string.lower()
    answer = sorted(my_string)
    return (''.join(answer))

    # 한줄로 요약
    return(''.join(sorted(my_string.lower())))

print(solution('Bcad'))
print(solution('heLLo'))
print(solution('Python'))