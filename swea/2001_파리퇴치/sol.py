import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 배열크기 M = 파리채크기

    # 빈 리스트 만들기
    numbers = []

    # 반복문 돌려 이중리스트형태로 input data 채우기
    for i in range(N):
        fly = list(map(int, input().split()))
        numbers.append(fly)

        
    # 배열 안에서 파리채의 시작점 잡기
    max_fly = 0
    for j in range(N-M+1):

        for k in range(N-M+1):
            total = 0 # 파리채로 죽일 수 있는 마리 수

            # 파리채를 크기대로 그리기
            for row in range(M): # 파리채의 가로
                for col in range(M): # 파리채의 세로 
                    total += numbers[j+row][k+col] 

            # 죽일 수 있는 총 마리수와 max_fly 비교
            if total > max_fly:
                max_fly = total

    print(f'#{tc} {max_fly}')


