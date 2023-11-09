import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 칠할영역의 개수
    N = int(input())

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
        else:
            blue.append(block_list[j])

    # print(red)
    # print(blue)

    # red, blue 구간 튜플로 표시해서 겹치는 구간 찾기
    # red 구간의 x축범위와 y축범위 튜플로 묶어 redpoint에 넣기
    red_point = []
    for k in range(len(red)):
        # x범위
        for rx in range(red[k][0], red[k][2]+1): 
            # y범위
            for ry in range(red[k][1], red[k][3]+1):
                # x값과 y값을 묶어 좌표형태로 만들기
                red_point.append((rx, ry))
            # print(red_point)

    # 방법 1
    # blue 구간 동일
    # blue_point = []
    # for k in range(len(blue)):
    #     # x범위
    #     for bx in range(blue[k][0], blue[k][2]+1):
    #         # y범위 
    #         for by in range(blue[k][1], blue[k][3]+1):           
    #             blue_point.append((bx, by))
    #         # print(blue_point)

    # # set&set으로 교집합 찾고 교집합의 길이 구하기
    # answer = len(set(red_point) & set(blue_point))
    # print(f'#{tc} {answer}')

    # 방법 2
    count = 0
    for k in range(len(blue)):
        # x범위
        for bx in range(blue[k][0], blue[k][2]+1):
            # y범위 
            for by in range(blue[k][1], blue[k][3]+1):           
                # red_point와 겹치는 좌표가 있다면 카운트
                if (bx, by) in red_point:
                    count += 1
    
    print(f'#{tc} {count}')

# # 다른방법 풀이 
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())         # 2개의 색칠영역

#     arr = [[0 for j in range(10)] for i in range(10)]
#     purple = 0

#     for i in range(N):      #첫번째는 빨강(1) # 두번째는 파랑(2)
#         r1, c1, r2, c2, color = list(map(int,input().split()))
        

#         for i in range(r1, r2 +1 ):
#             for j in range(c1, c2 +1):
#                 if arr[i][j] == 0:
#                     arr[i][j] += color

#                 elif arr[i][j] != color:  # 서로 다른 색이면 3으로 바꾼다
#                     arr[i][j] = 3

#                 if arr[i][j] == 3:
#                     purple += 1

#     print(f'#{tc} {purple}')