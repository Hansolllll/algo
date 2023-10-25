def solution(n):
    if n % 2 :
        even_numbers = list(range(2, n, 2))

    else:
        even_numbers = list(range(2, n+1, 2))

    answer = 0
    for even_number in even_numbers:
        answer = answer + even_number

    return answer

# 다른 풀이법

def solution(n):
    numbers = range(2, n+1, 2)
    return sum(numbers)


print(solution(10))
print(solution(4))