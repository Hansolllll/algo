def solution(price, money, count):
    total = 0
    for i in range(count):
        charge = price * (i+1)
        total += charge
    return (total-money) if total>money else 0


print(solution(3, 20, 4))

