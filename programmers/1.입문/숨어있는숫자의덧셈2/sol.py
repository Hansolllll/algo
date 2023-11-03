def solution(my_string):
    stack = []
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            # 스택이 비었을 때 - 추가
            if len(stack) == 0:
                stack.append(my_string[i])
                idx = i # 인덱스 저장하고 붙어있는 숫자인지 판단할 때 사용
            
            # 스택이 차있을 때 -     
            else:
                # 현재 인덱스 번호와 추가한 숫자 인덱스 번호 차이가 1이라면(붙어있다면)
                if i - idx == 1:
                    stack[-1] = stack[-1] + my_string[i]
                    idx = i
                # 붙어있는 숫자가 아니라면 
                else:
                    stack.append(my_string[i])
                    idx = i

    stack = map(int, stack)
    return sum(stack)


# replace 이용
def solution(my_string):
    sum_num = 0
    
    for i in my_string:
        if not i.isdigit():        # my_string의 글자하나씩 출력해서 그것이 숫자가 아니라면
            my_string = my_string.replace(i, ' ')  #공백으로 대체해준다

    for j in my_string.split():     # 공백으로 잘라주고
        sum_num += int(j)           # mystring 값이 문자이므로 정수형태로 변환하여 더해준다
        
    return sum_num

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123Z'))