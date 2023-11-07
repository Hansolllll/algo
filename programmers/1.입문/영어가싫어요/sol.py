def solution(numbers):
    # 인덱스 만들기(단어가 의미하는 숫자 = 인덱스)
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for char in eng:
        if char in numbers:
            # 반복문으로 eng 내부 숫자가 포함되는지 확인하고 변환
           numbers = numbers.replace(char, str(eng.index(char)), numbers.count(char))
        
    return int(''.join(numbers))

    # for i in range(len(eng)):
    #     if eng[i] in numbers:
    #         numbers = numbers.replace(eng[i], str(i))

print(solution('onetwothreefourfivesixseveneightnine'))
print(solution('onefourzerosixseven'))