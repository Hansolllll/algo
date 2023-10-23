def solution(n):
    num_list1 = [num1 for num1 in range(n+1)]
    total = 0
    for num1 in num_list1:
        num_list2 = [num2 for num2 in range(num1+1)]
        count = 0
        for num2 in num_list2:
            try:
                num1 % num2
                if num1 % num2 == 0:
                    count += 1  
            except:
                continue

        if count >= 3:
            total += 1

    return total

print(solution(10))
print(solution(15))