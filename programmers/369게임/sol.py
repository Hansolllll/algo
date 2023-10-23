def solution(order):
    count = 0
    for char in str(order):
        if int(char) == 3 or int(char) == 6 or int(char) == 9:
            count += 1  

        
    return count

print(solution(3))
print(solution(29423))