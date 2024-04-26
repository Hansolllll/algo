def solution(my_string):
    my_list = list(my_string)
    result = 0
    for string in my_list:
        try:
            result = result + int(string)
            continue
        except:
            continue
        else:
            return result
    answer = result
    return answer

def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdigit():
            answer += int(char)

    return answer

def solution(my_string):
    answer = 0

    for char in my_string:
        try:
            answer += int(char)
        except:
            continue

    return answer

def solution(my_string):
    answer = 0

    for char in my_string:
        if not(ord('A') <= ord(char) <= ord('z')):
            answer += int(char)

    return answer

def solution(my_string):
    nums = '0123456789'
    total = 0
    for char in my_string:
        if char in nums:
            total += int(char)
    return total
    
print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))