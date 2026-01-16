from collections import deque

def solution(board, moves):
    # 스택보드로 변환
    blen = len(board)
    stack_board = []
    for i in range(blen):
        stack = deque()
        for j in range(blen):
            if board[j][i] > 0:
                stack.append(board[j][i])
        stack_board.append(stack)
        
    # 바구니 로직
    answer = 0
    bucket = []
    for move in moves:
        move -= 1
        if stack_board[move]:
            item = stack_board[move].popleft()
            if bucket and bucket[-1] == item:
                answer += 2
                bucket.pop()
            else:
                bucket.append(item)
    
    return answer