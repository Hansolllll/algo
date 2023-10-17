import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K 최대 이동가능한 정류장 수
    # N 종점
    # M 충전기 있는 정류장 수
    K, N, M = map(int, input().split()) # 변수 가져오기
    stations = list(map(int, input().split())) # 정류장 번호 가져오기  

    charging = 0
    now = 0

    if K < N: # 바로 도착 못할 경우
        while now < N:
            for i in range(now+K, now, -1): #이동가능한 범위 내 충전소 찾기
                if i >= N: # 이동가능한 거리가 종점넘을 경우
                    now = N
                    break
                if i in stations: # 이동가능 거리가 종점 안넘을 경우
                    now = i 
                    charging += 1
                    break

            else: # 범위안에 이동할 정류장이 없는경우
                charging = 0
                now = N
    else: # 바로 도착 가능한경우
        now = N 
        charging = 0            
    

    print(f'#{tc}, {charging}')

