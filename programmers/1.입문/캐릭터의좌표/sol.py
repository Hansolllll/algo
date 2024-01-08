def solution(keyinput, board):
    # 기본좌표 잡기
    x, y = 0, 0
    x_limit = board[0]//2
    y_limit = board[-1]//2

    # 모든 방향에서 board 범위내에 있을 때만 x, y값 연산
    for _ in keyinput:
        if _ == 'left' and abs(x-1) <= x_limit:
            x -= 1
        elif _ == 'right' and abs(x+1) <= x_limit:
            x += 1
        elif _ == 'up' and abs(y+1) <= y_limit:
            y += 1
        elif _ == 'down' and abs(y-1) <= y_limit:
            y -= 1
    
    return [x, y]

print(solution(["left", "right", "up", "right", "right"], [11,11]))
print(solution(["down", "down", "down", "down", "down"], [7,9]))