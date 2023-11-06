def solution(bin1, bin2):
    # 내장함수 이용
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

    # 내장함수 없이 풀이
    numbers = []
    # 2진수를 정수형태로 만들어서 더하기
    number = int(bin1) + int(bin2)
    # numbers 리스트에 넣기
    for num in str(number):
        numbers.append(int(num))
    
    # numbers 뒤부터 2보다 크면 2빼고 앞 숫자에 1더하기
    for i in range(len(numbers)-1, 0, -1):
        while numbers[i] > 1:
            numbers[i] -= 2
            numbers[i-1] += 1
    # 맨 앞자리는 자릿수를 추가해야하므로 조건문으로 만들기
    if numbers[0] > 1:
        numbers[0] -= 2
        numbers.insert(0, 1)

    return ''.join(map(str, numbers))


  
# bin() : 10->2진수 
# oct(): 10->8진수
# hex(): 10->16진수
# int(,입력숫자 진수): 다른 진수->10진수

print(solution('10', '11'))
print(solution('1001', '1111'))