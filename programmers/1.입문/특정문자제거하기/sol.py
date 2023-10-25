def solution(my_string, letter):
    string_list = []
    for strings in my_string:
        if strings != letter:
            string_list.append(strings)
    answer = ''.join(string_list)

    return answer

def solution(my_string, letter):
    answer = my_string.replace(letter, '')

    return answer 

def solution(my_string, letter):
    answer = ''

    for string in my_string:
        if string != letter:
            answer += string

    return answer

print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))