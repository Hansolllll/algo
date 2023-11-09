import sys
sys.stdin = open('input.txt')

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
        

