def solution(s):
    s = s.replace('P', 'p')
    s = s.replace('Y', 'y')

    if s.count('y') == s.count('p'):
        return True
    else: 
        return False

    # 컴프리헨션
    return True if s.count('y') == s.count('p') else False



print(solution("pPoPooyY"))
print(solution("oooav"))
print(solution("Pyy"))
