def solution(s):
    if len(s) != 4 or len(s) != 6:
        return False
    for char in s:
        if char.isdigit()==False:
            return False
    return True

print(solution('a234'))
print(solution('1234'))