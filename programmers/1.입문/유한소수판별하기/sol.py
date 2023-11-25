import math

def solution(a, b):
    # 최대공약수가 있다면 분모 분자 반복해서 나누기
    while math.gcd(a, b) != 1:
        div = math.gcd(a, b)
        a = int(a//div)
        b = int(b//div)

    # 최대공약수로 다 나눈 후 정수라면(분모가 1이라면) 유한소수 
    if b == 1:
        return 1

    num_list = []
    # 반복문 통해 중복되지 않는 약수만 리스트에 넣기
    for num in range(2, b+1):
        while b % num == 0:
            if num not in num_list:
                num_list.append(num)
            b //= num

    # 리스트가 2와 5로만 구성되어 있지다면 1, 아니면 2 반환
    if num_list == [2, 5] or num_list == [2] or num_list == [5]:
        return 1
    else:
        return 2


print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))
print(solution(3, 4))
print(solution(3500, 500))
