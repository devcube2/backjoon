def solution(keyinput, board):
    x, y = board[0] // 2, board[1] // 2
    result_x, result_y = 0, 0
    for dir in keyinput:
        if dir == "left":
            if x - 1 >= 0:
                x -= 1
                result_x -= 1
        elif dir == "right":
            if x + 1 < board[0]:
                x += 1
                result_x += 1
        elif dir == "down":
            if y - 1 >= 0:
                y -= 1
                result_y -= 1
        elif dir == "up":
            if y + 1 < board[1]:
                y += 1
                result_y += 1
    return [result_x, result_y]