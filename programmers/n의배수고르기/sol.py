def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)  

    return answer


# 아래는 pop을 이용해서 해결해보려고했는데 pop하는 동작때문에 인덱스가 일정하지 않아서 에러뜸
# def solution(n, numlist):
#     for i in range(len(numlist)):
#         if numlist[i] % n != 0:

#             numlist.pop(i)
#         else: 
#             continue

#     return numlist



print(solution(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution(5,[1, 9, 3, 10, 13, 5]))
print(solution(12,[2, 100, 120, 600, 12, 12]))