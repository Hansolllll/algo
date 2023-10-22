def solution(my_string, num1, num2):    
    my_list = []
    for char in my_string:
        my_list.append(char)
    temp = [my_string[num1], my_string[num2]]

    my_list[num1] = temp[1]
    my_list[num2] = temp[0]
    return ''.join(my_list)


    # for char in my_string:
    #     a = my_string[num1]
    #     b = my_string[num2]

    #     my_string = my_string.replace(my_string[num1], b)
    #     my_string = my_string.replace(my_string[num2], a)

    # return my_string

print(solution('hello', 1, 2))
print(solution('I love you', 3, 6))