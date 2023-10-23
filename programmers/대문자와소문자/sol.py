def solution(my_string):
    answer = ''
    for char in my_string:
        if char.islower() == True:
            answer += char.upper()
        elif char.isupper() == True:
            answer += char.lower()

    return answer


print(solution("cccCCC"))
print(solution("abCdEfghIJ"))