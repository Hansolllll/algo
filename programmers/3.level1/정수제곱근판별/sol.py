def solution(n):
    # 0.5 제곱한 수가 int를 씌운 값과 같다면 +1한 다음 제곱리턴 아니면 -1 리턴
    return int((n**0.5+1)**2) if n**0.5 == int(n**0.5) else -1




print(solution(121))
print(solution(3))