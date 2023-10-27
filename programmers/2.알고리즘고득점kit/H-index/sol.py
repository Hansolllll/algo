def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            return citations[i] 


    # 이중반복문으로 i인덱스 이상인 수를 카운트 해서 count_list에 넣기(H-index에 대한 이해부족)
    # answer = []
    # count_list = []
    
    # for i in range(len(citations)):
    #     count = 0
    #     for j in range(len(citations)):
    #         if citations[j] >= citations[i]:
    #             count += 1
    #     count_list.append(count)

    # for k in range(len(citations)):
    #     if count_list[k] >= citations[k]:
    #         answer.append((citations[k], count_list[k]))

    # return max(answer)[0]
    
    # gpt 나쁜놈
    # citations.sort()  # 논문 인용 횟수 배열을 오름차순으로 정렬
    # n = len(citations)
    
    # for i in range(n):
    #     if citations[i] >= n - i:
    #         return n - i
    
    # return 0


print(solution([3, 0, 6, 1, 5]))