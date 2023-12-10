def solution(common):
    # 등차수열이라면
    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        return common[-1] + diff
    # 등비수열이라면
    elif common[1]//common[0] == common[2]//common[1]:
        diff = common[1]//common[0]
        return int(common[-1]*diff)


print(solution([1,2,3,4]))
print(solution([2,4,8]))