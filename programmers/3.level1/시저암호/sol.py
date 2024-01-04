# 런타임 에러
def solution(s, n):
    answer = ''
    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in s:
        if char in ['z', 'Z']:
            answer += char_list[n-1]
        elif char.islower():
            idx = char_list.index(char)
            answer += char_list[idx+n]
        elif char.isupper():
            idx = char_list.index(char.lower())
            answer += (char_list[idx+n]).upper()
        else:
            answer += ' '
    return answer

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))