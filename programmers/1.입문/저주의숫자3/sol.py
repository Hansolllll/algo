# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 
# 정수 n이 매개변수로 주어질 때, 
# n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.

# 소생 불가 코드
# def solution(n):
#     answer = 1
#     for num in range(1, n+1):
#         while answer % 3 == 0 or '3' in str(num):
#             answer += 1
#     return answer

def solution(n):
    answer = 0
    count = 0
    while count < n:
        answer += 1
        if '3' in str(answer) or answer % 3 == 0:
            continue
        count += 1
    return answer

# set이용
def solution(n):
    a = []
    for i in range(1, 250):
        if i % 3 != 0 and '3' not in str(i):
            a.append(i)

    answer = {}
    # answer = {key+1: value for key, value in enumerate(a)}

    for key, value in enumerate(a):
        answer[key+1] = value 

    return answer[n]
# set이용 2
def solution(n):
    x = [i for i in range(1, 200) if i % 3 != 0]
    y = [i for i in range(1, 200) if '3' not in str(i)]

    answer = list(set(x) & set(y))
    return answer[n-1]
    
print(solution(15))
print(solution(15))
print(solution(40))