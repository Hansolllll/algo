def solution(numbers, k):
    # k가 홀수일 때
    if k % 2 != 0:
        idx = (k-1)//2
        return numbers[idx]

    # k가 짝수일때
    else:
        
        

# 테스트케이스 절반은 fail
    # num_list = numbers * 50
    # count = 0
    # for i in range(0,len(num_list), 2):
    #     count += 1
    #     if count == k:
    #         return num_list[i]


print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))