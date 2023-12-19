def solution(board):
    answer = 0
    bomb = []
    for i in range(len(board)):
        for k in range(len(board)):
            
            if board[i][k] == 1:
                bomb.append((i,k))
    
    for _ in bomb:
        i = _[0]
        k = _[-1]
        
        if _[0] == 0:
            limit_x = range(2)
        elif _[0] == len(board)-1:
            limit_x = range(-1, 1)
        else:
            limit_x = range(-1,2)
        
        if _[-1] == 0:
            limit_y = range(2)
        elif _[-1] == len(board)-1:
            limit_y = range(-1, 1)
        else:
            limit_y = range(-1,2)
            
        for x in limit_x:
            for y in limit_y:
                board[i+x][k+y] = 3
                
    for i in range(len(board)):
        for k in range(len(board)):
            if board[i][k] == 0:
                answer += 1
    return answer
    
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))

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
