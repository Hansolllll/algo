def solution(numbers):

    # numbers 내의 숫자를 3번 반복한 수를 만들기 위해 문자로 변환
    numbers = list(map(str, numbers))
    
    # sort(key=None, reverse=False)가 기본형, key를 기준으로 정렬하는 sort 이용하기
    numbers.sort(key = lambda x : x*3, reverse=True) # lambda 이용해 3번 반복된 문자열 기준으로 정렬
    
    # 리스트 내 값을 문자열로 반환
    # numbers 내의 모든 변수가 0일 경우 '000'반환될 수 있으므로 정수화-문자화 거치기
    return str(int(''.join(numbers))) 

    # '000'인 경우에서 걸림
    # for i in numbers:
    #     answer += i

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))




