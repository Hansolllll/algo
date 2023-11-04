def solution(n):
    answer = []

    for i in range(2, n+1):
        while n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i
    return answer

# answer = []

#     for i in range(1, n):
#         if n % i == 0:
#             answer.append(n//i)
#             answer.sort()


#     return answer

print(solution(12))
print(solution(17))
print(solution(420))