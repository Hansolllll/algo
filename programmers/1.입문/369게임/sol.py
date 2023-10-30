def solution(order):
    count = 0
    # order내의 문자가 3,6,9 일때 카운트 추가
    for char in str(order):
        if int(char) == 3 or int(char) == 6 or int(char) == 9:
            count += 1  
    return count

# 369게임을 이해 잘 하신 분 
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + 
order.count('6') + order.count('9')

# 한줄장인
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

print(solution(3))
print(solution(29423))