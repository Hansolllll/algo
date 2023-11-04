def solution(my_string):
    # 공백 기준으로 split
    my_string = my_string.split()

    # 첫번째 숫자를 기준값으로 잡기
    total = int(my_string[0])
    # index out of range 피하기
    for i in range(len(my_string)-1):
        
        # my_string에서 연산 기호 나오면 total에서 누적 계산
        if my_string[i] == '+':
            total += int(my_string[i+1])
        elif my_string[i] == '-':
            total -= int(my_string[i+1])
    
    return total


# # 하나의 기호만 계속 사용된다고 착각
#     # my_string에서 공백 제거
#     my_string = my_string.replace(' ', '')
#     # my_string 안에서 숫자 찾아서 number이라는 리스트 만들기
#     number = [int(num) for num in my_string if num.isdigit()]

#     # +기호 포함한 경우 sum사용
#     if '+' in my_string:
#         return sum(number)
#     # -기호 포함한 경우 2번째 숫자부터 끝까지 더한다음 첫 숫자에서 빼주기
#     else:
#         return number[0] - sum(number[1:])


print(solution('34 + 4 - 1'))