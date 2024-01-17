from string import ascii_lowercase, ascii_uppercase

def solution(s, n):
    answer = ''
    lower_list = list(ascii_lowercase)
    upper_list = list(ascii_uppercase)

    for char in s:
        # 소문자인 경우
        if char.islower():
            idx = lower_list.index(char) 
            # n번 이동했을 때 z 넘는경우
            if idx + n > 25:
                answer += lower_list[idx+n-26]
            else:
                answer += lower_list[idx+n]
        # 대문자인 경우 
        elif char.isupper():
            idx = upper_list.index(char)
            # n번 이동했을 때 z 넘는경우
            if idx + n > 25:
                answer += upper_list[idx+n-26]
            else:
                answer += upper_list[idx+n]
        # 공백인 경우
        else:
            answer += ' '
    return answer


# 2차시도: 1개 빼고 런타임 에러
# def solution(s, n):
#     answer = ''
#     char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
#     for char in s:
#         if char.islower():
#             if char == 'z':
#                 answer += char_list[n-1]
#             else:
#                 idx = char_list.index(char)
#                 answer += char_list[idx+n]
#         elif char.isupper():
#             if char == 'Z':
#                 answer += (char_list[n-1]).upper()
#             else:
#                 idx = char_list.index(char.lower())
#                 answer += (char_list[idx+n]).upper()
#         else:
#             answer += ' '
#     return answer

# 1차 시도: 런타임에러 
# def solution(s, n):
#     answer = ''
#     char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # for char in s:
    #     if char in ['z', 'Z']:
    #         answer += char_list[n-1]
    #     elif char.islower():
    #         idx = char_list.index(char)
    #         answer += char_list[idx+n]
    #     elif char.isupper():
    #         idx = char_list.index(char.lower())
    #         answer += (char_list[idx+n]).upper()
    #     else:
    #         answer += ' '
    # return answer

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))