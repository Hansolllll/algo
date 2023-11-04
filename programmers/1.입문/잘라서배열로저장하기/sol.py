def solution(my_str, n):
    result = []
    for i in range(0,len(my_str),n):
        result.append(my_str[i:i+n])

    return result

print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))