def solution(board):
    answer = 0
    bomb = []
    # 길이가 1일 때
    if board == [[0]]:
        return 1
    elif board == [[1]]:
        return 0

    else:
        # 지뢰 위치 찾아서 bomb 안에 넣기
        for i in range(len(board)):
            for k in range(len(board)):
        
                if board[i][k] == 1:
                    bomb.append((i,k))

        # i는 지뢰 x좌표, k는 지뢰 y좌표일 때 지뢰 위치에 따라 범위 정해주기
        for _ in bomb:
            i = _[0]
            k = _[-1]
            
            # 지뢰가 첫번째 행에 있을 겅우
            if _[0] == 0:
                limit_x = range(2)
            # 지뢰가 마지막 행에 있을 경우     
            elif _[0] == len(board)-1:
                limit_x = range(-1, 1)
            # 지뢰가 사이 행에 있을 경우
            else:
                limit_x = range(-1,2)
            
            # 지뢰가 첫번째 열에 있을 경우
            if _[-1] == 0:
                limit_y = range(2)
            # 지뢰가 첫번째 열에 있을 경우
            elif _[-1] == len(board)-1:
                limit_y = range(-1, 1)
            # 지뢰가 그 사이 열에 있을 경우
            else:
                limit_y = range(-1,2)
            
            # 위에서 정해진 x y축 범위 안의 값들을 3으로 바꾸기(위험 지역)
            for x in limit_x:
                for y in limit_y:
                    board[i+x][k+y] = 3

        # 3으로 바뀌지 않은 지대만 안전지대로 카운트 
        for i in range(len(board)):
            for k in range(len(board)):
                if board[i][k] == 0:
                    answer += 1
        return answer
    
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
print(solution([[0]]))
print(solution([[1]]))

# def solution(board):
#     answer = 0
#     # board 크기 확인
#     rows, cols = len(board), len(board[0])

#     # board를 for문을 돌려 1 찾기
#     for i in range(rows):
#         for j in range(cols):
#             if board[i][j] == 1:
#                 continue
            
#             # 안전지대를 체크할 변수 선언
#             count = 0

#             # 지뢰 근처의 범위 설정(max, min 한 이유는 out of range 를 피하기 위함)(이게 되네..?)
#             for x in range(max(0, i - 1), min(rows, i + 2)):
#                 for y in range(max(0, j - 1), min(cols, j + 2)):
#                     # 그 범위에 맞게 확인 후 count
#                     count += board[x][y]
#             # 지뢰의 범위가 닿지 않는 곳은 0이므고 그 갯수를 answer에 append
#             if count == 0:
#                 answer += 1
    # return answer
