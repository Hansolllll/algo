def solution(s):
    num_list = list(map(int, s.split(' ')))
    return f'{min(num_list)} {max(num_list)}'

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
