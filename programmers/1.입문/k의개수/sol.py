def solution(i, j, k):
    total = 0
    # i에서 j까지의 범위 만들기
    for num in range(i, j+1):
        # 범위 내 숫자와 k를 문자열로 바꿔서 count 메서드 사용
        count = str(num).count(str(k))
        total += count

    return total

print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))