def solution(n):
    numlist = [num for num in range(1, n+1)]
    for num in numlist:
        if (6*num) % 6 == 0 and (6*num) % n == 0:
            return num
            break


print(solution(6))
print(solution(10))
print(solution(4))