def solution(polynomial):
    polynomial = polynomial.replace(' ', '')
    polynomial = polynomial.split('+')

    # # x 앞에 숫자가 없으면 1을 넣어줘라
    i = 0
    while i < len(polynomial):
        if polynomial[i] == 'x' :
            polynomial[i] = '1x'
        i += 1

    # return polynomial

    # # 숫자 뒤에 x 가 있는 수를 x, 숫자 뒤에 x가 없는 수를 y로 할당
    x = []
    y = []
    
    for char in polynomial:
        if char[-1] == 'x':
            x.append(int(char[:-1]))
        else:
            y.append(int(char))

    return x, y


print(solution("3x + 7 + x")) #"4x + 7"
print(solution("x + x + x")) #"3x"
print(solution("7x + 4 + 9 + 5x")) #"12x + 13"
print(solution("10x")) #"10x"
