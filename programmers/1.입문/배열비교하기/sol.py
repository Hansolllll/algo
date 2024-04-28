def solution(arr1, arr2):
    # 둘의 길이가 같지 않다면 
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    # 둘의 길이가 같다면
    else:
        # 합이 같다면 0, arr2의 합이 크다면 -1, arr1의 합이 크다면 1
        return 0 if sum(arr1) == sum(arr2) else -1 if sum(arr2) > sum(arr1) else 1



print(solution([49,13],[70,11,12]))
print(solution([100,17,84,1],[55,12,65,36]))
print(solution([1,2,3,4,5],[3,3,3,3,3]))
