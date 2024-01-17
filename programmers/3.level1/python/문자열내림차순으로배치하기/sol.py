def solution(s):
    upper = []
    lower = []

    for char in s:
        if char.isupper() :
            upper.append(char)
        else:
            lower.append(char)

    return ''.join(sorted(lower, reverse=True) + sorted(upper, reverse=True))


print(solution('Zbcdefg'))