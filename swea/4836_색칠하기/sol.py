import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 칠할영역의 개수

    block_list = [] # input 데이터 붙여서 긴 데이터 만들기
    red = [] # 빨간색으로 칠할 구간 
    blue = [] # 파란색으로 칠할 구간

    # blocklist에 input데이터 다 넣기
    for i in range(N):
        numbers = list(map(int, input().split()))
        block_list.append(numbers)
    
    # 빨갛게 칠할 구간과 파랗게 칠할 구간 나누기
    for j in range(len(block_list)):
        if block_list[j][4] == 1:
            red.append(block_list[j])
        elif block_list[j][4] == 2:
            blue.append(block_list[j])

    # red, blue 구간 튜플로 표시해서 겹치는 구간 찾기
    # red 구간의 x축범위와 y축범위 튜플로 묶어 redpoint에 넣기
    redpoint = []
    for k in range(len(red)):
        for rx in range(red[k][0], red[k][2]+1):
            for ry in range(red[k][1], red[k][3]+1):
                redpoint.append((rx, ry))

    # blue구간의 x축범위와 y축범위를 튜플로 묶은 것이 
    # redpoint내에 존재하는지 확인한 후 카운트 
    count = 0
    for k in range(len(blue)):
        for bx in range(blue[k][0], blue[k][2]+1):
            for by in range(blue[k][1], blue[k][3]+1):
                if (bx, by) in redpoint:
                    count += 1

    print(f'#{tc} {count}')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # N :칠할 영역

    #칠할공간 만들기 (board)
    board = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(N):
        color_data = list(map(int, input().split()))

        left_top_x = color_data[0] # 시작점 x좌표
        left_top_y = color_data[1] # 시작점 y좌표
        right_bottom_x = color_data[2] # 끝점 x좌표
        right_bottom_y = color_data[3] # 끝점 y좌표
        color = color_data[4] # 빨강파랑 구분데이터

        # 색칠시작
        # 시작점 ~ 끝점 사이의 x, y 값 매치해서 보드좌표에 컬러 넣기
        for x in range(left_top_x, right_bottom_x+1):
            for y in range(left_top_y, right_bottom_y+1):
                board[x][y] += color
            
    count = 0
    # 보드좌표에서 값이 3인 것들 카운트하기(빨강 :1, 파랑:2 >> 보라:1+2)
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 3:
                count += 1

    print(f'#{tc} {count}')  
        

