def solution(a, b):
    # 각 월별 날짜, 요일 딕셔너리로 만들기
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    total = 0
    # a 이전달까지의 날짜 더하기 
    # ex. 5월 3일 -> 4월까지의 날짜 + 3일 
    for i in range(1, a):
        total += month[i]

    # 반복문 밖에서 b 더하기 
    total += b
    
    # (총 날짜를 7로 나눈 나머지 값)을 7로 나눈 후 -1 번째의 요일 반환 
    return day[(total % 7)-1]

print(solution(5, 24))