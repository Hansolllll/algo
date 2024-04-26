def solution(arr, n):
    # 길이가 홀수라면
    if len(arr) % 2:
        return [arr[i]+n if i % 2 == 0 else arr[i] for i in range(len(arr))]
        # for i in range(len(arr)):
        #     if i % 2 == 0:
        #         arr[i] += n
            
    # 짝수라면
    else:
        return [arr[i]+n if i % 2 else arr[i] for i in range(len(arr))]
        # for i in range(len(arr)):
        #     if i % 2:
        #         arr[i] += n
    # return arr
print(solution([49, 12, 100, 276, 33],27))
