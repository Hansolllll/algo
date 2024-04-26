# def solution(rsp):
#     result = []
#     for i in rsp:
#         if i == '2':
#             result.append('0')
#         elif i == '0':
#             result.append('5')
#         else:
#             result.append('2')
    
#     answer = ''.join(result)
#     return answer

# def solution(rsp):
#     answer = ''
#     for char in rsp:
#         if char == '2':
#             answer += '0'
#         elif char == '0':
#             answer += '5'
#         else:
#             answer += '2'
    
#     return answer

def solution(rsp):
    answer = ''

    rsp_dict = {
        '2': '0',
        '0': '5',
        '5': '2',
    }

    for char in rsp:
        answer += rsp_dict[char]

    return answer

def solution(rsp):
    rsp_dict = {'2':'0', '0':'5', '5':'2'}
    return ''.join([rsp_dict[num] for num in rsp])
    
print(solution('2'))
print(solution('205'))