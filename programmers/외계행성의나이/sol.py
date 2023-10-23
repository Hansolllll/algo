from string import ascii_lowercase

def solution(age):
    answer = ''
    alpha = list(ascii_lowercase)

    age = str(age)
    for char in age:
        answer += alpha[int(char)]
    return answer
 

print(solution(23))
print(solution(51))