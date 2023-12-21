def solution(s):
    if len(s) = 4 or len(s) = 6:
        for char in s:
            if char.isdigit()==False:
                return False
        return True
    return False

print(solution('a234'))
print(solution('1234'))