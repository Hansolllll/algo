def solution(array, n):
    answer = 100
    for num in array:
        if abs(num - n) < abs(answer - n):
            answer = num
        elif abs(num - n) == abs(answer - n):
            answer = min(num, answer)
    return answer

    
# sort 이용
def solution(array, n):
    result = []                     # 17, 10 ,10
    array = sorted(array)           # sorted를 했기 때문에 알아서 더 작은 값이 반환
    for i in array:                 # 3, 10 ,28 반환
        result.append(abs(n - i))   # n인 20과의 차이를 절대값을 만들어 result배열에 append
   
    
    ans = result.index(min(result))  # result의 최소값의 인덱스 반환
    return array[ans]     

        
print(solution([3, 10, 30], 20))
print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))