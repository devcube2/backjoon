def solution(board):    
    xmax = len(board[0])
    ymax = len(board)
    new_board = [[0] * xmax for _ in range(ymax)]
    for y in range(ymax):
        for x in range(xmax):
            if board[y][x] == 1:
                for ny, nx in [[y-1, x], [y+1, x], [y, x-1], [y, x+1], [y-1, x-1], [y-1, x+1], [y+1, x-1], [y+1, x+1]]:
                    if ny >= 0 and ny < ymax and nx >= 0 and nx < xmax:
                        new_board[ny][nx] = 1
                new_board[y][x] = 1    
    return (xmax * ymax) - sum([sum(line) for line in new_board])