def solution(num, k):
    #반복문 이용
    for i in str(num):
        if i == str(k):
            return (str(num)).index(i) + 1 # 자릿수니까 +1
    else:
        return -1

    #문자열 메소드 이용
    num = str(num)
    k = str(k)
    if num.find(k) == -1: # 만약 문자열 내에 없다면 
        return -1
    else:
        return num.find(k) + 1 # 있다면 자릿수로 출력

print(solution(29183, 1))
print(solution(232442, 4))
print(solution(123456, 7))