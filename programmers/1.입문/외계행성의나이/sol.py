# 알파벳 정렬하는 함수 이용하기 위해 import 
from string import ascii_lowercase

def solution(age):
    # 알파벳 리스트 만들고 그 인덱스에 해당하는 값 문자열형태로 더하기
    answer = ''
    alpha = list(ascii_lowercase)

    age = str(age)
    for char in age:
        answer += alpha[int(char)]
    return answer
 

print(solution(23))
print(solution(51))