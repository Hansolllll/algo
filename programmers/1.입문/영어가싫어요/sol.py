def solution(numbers):
    # 인덱스 만들기(단어가 의미하는 숫자 = 인덱스)
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for char in eng:
        if char in numbers:
            # 반복문으로 eng 내부 숫자가 포함되는지 확인하고 변환
           numbers = numbers.replace(char, str(eng.index(char)), numbers.count(char))
        
    return int(''.join(numbers))

# 딕셔너리 이용
def solution(numbers):
    num = {
        'one' : 1 , 'two' : 2, 'three' : 3,
        'four' : 4, 'five' : 5, 'six' : 6,
        'seven' : 7, 'eight' : 8, 'nine': 9 
        'zero' : 0
    }

    answer = numbers  

#원소(키/값 쌍)들을 얻으려면 이름 뒤에 .items()를 쓰면 됩니다.
# dict_items([('one', '1'), ('two', '2') ... 튜플로 반환
# k에는 key 값, v에는 value값 할당

    for k, v in num.items():
        answer = answer.replace(k, str(v))
        # replace는 문자열을 변경하는 함수
    return int(answer)

# 딕셔너리 이용 2
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])
    return int(numbers)

# enumerate 이용
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)


print(solution("onefourzerosixseven"))    
print(solution('onetwothreefourfivesixseveneightnine'))
print(solution('onefourzerosixseven'))