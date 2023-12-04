def solution(polynomial):
    # 문자사이 공백 제거하고 + 기준으로 split
    polynomial = polynomial.replace(' ', '')
    polynomial = polynomial.split('+')

    x_num = []
    const = []

    # split한 구성중 'x'가 있다면 계수 1 넣어주기
    for i in range(len(polynomial)):
        if polynomial[i] == 'x':
            polynomial[i] = '1x'

    # 'x'로 끝난다면 x전의 숫자까지 계수로 간주하고 x_num에 넣기
    # 아니라면 상수로 간주하고 const에 넣기
    for num in polynomial:
        if num[-1] == 'x':
            x_num.append(num[0:-1])
        else:
            const.append(num)
    
    # 리스트 내 숫자들 합구하기
    x_num = sum(map(int, x_num))
    const = sum(map(int, const))

    # f-string으로 경우에 맞는 수식 반환하기    
    if  x_num == 0:
        if const != 0:
            return f'{const}'
        else:
            return 0  

    elif x_num == 1:
        if const != 0:
            return f'x + {const}'
        else:
            return 'x'

    elif x_num != 0:
        if const != 0:
            return f'{x_num}x + {const}'
        else: 
            return f'{x_num}x'


print(solution("3x + 7 + x"))
print(solution("x + x + x"))