def solution(my_string, num1, num2):    
    my_list = []
    # my_list에 문자열 반복해서 추가
    for char in my_string:
        my_list.append(char)
    
    # 필요한 인덱스 값은 temp에 따로 저장
    temp = [my_string[num1], my_string[num2]]

    # 리스트 내에서 재할당
    my_list[num1] = temp[1]
    my_list[num2] = temp[0]
    return ''.join(my_list)

def solution(my_string, num1, num2):
    my_list = [my_string[i] for i in range(len(my_string)) if i not in [num1, num2]]
    my_list.insert(num1, my_string[num2])
    my_list.insert(num2, my_string[num1])
    return ''.join(my_list)

    # replace 메소드 이용해 해결해보려 했으나, 중간 인덱스의 값은 바꿀 수 없음
    # for char in my_string:
    #     a = my_string[num1]
    #     b = my_string[num2]

    #     my_string = my_string.replace(my_string[num1], b)
    #     my_string = my_string.replace(my_string[num2], a)

    # return my_string

print(solution('hello', 1, 2))
print(solution('I love you', 3, 6))