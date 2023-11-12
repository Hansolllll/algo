def solution(numbers, k):
    # k가 홀수일 때
    if k % 2 != 0:
        idx = (k-1)//2
        return numbers[idx]

    # k가 짝수일때
    else:

# ??????????????
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

# 풀이 2
import math

def solution(numbers,k):
    n= int(math.ceil((2*k)/len(numbers)))
    answer = []

    for _ in range(n):    
        for i in numbers:
            answer.append(i)  # [1 2 3 4 5 6 1 2 3 4 5 6]  
    
    return answer[k*2-2]    


# 환형큐 이용
from collections import deque

def solution(numbers, k):
    n = len(numbers) 일곱번째로 공을 던진 사람
    answer = [] # 3 1 3 1 3 1 3 1 3 1 3

    # 일단 deque를 써서 원형 큐 만들기
    circular_queue = deque(numbers)
    for i in range(k):
        # 두칸씩 미루기 ( . . . 1 2 3 4 1 2 3 4 1 2 3 4 . . . )
        circular_queue.rotate(-2)
        answer.append(circular_queue[0]) # 3 1 3 1 3 1 3 1

    return answer[k-2]

print(solution([1, 2, 3, 4], 2)) #[3, 1]
print(solution([1, 2, 3, 4, 5, 6], 5))  # [3, 5, 1, 3, 5]
print(solution([1, 2, 3], 3))  # [3, 2, 1]

# 노가다 
    # num_list = numbers * 500
    # count = 0
    # for i in range(0,len(num_list), 2):
    #     count += 1
    #     if count == k:
    #         return num_list[i]


print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5)) 4 2
print(solution([1, 2, 3], 3)) 2 1