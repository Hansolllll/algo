def solution(my_string):
    my_list = []

    for string in my_string:
        my_list.insert(0, string)

    answer = ''.join(my_list)

    return answer


print(solution('jaron'))
print(solution('bread'))