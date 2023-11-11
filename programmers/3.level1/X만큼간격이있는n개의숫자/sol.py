def solution(x, n):
    # 방법 1(런타임 에러)
    return [i for i in range(x, x*n-1, x)] if x<0 else [i for i in range(x, x*n+1, x)]
  
    # 방법 2
    return [x * i for i in range(1, n + 1)]



print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))