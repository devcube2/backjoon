import sys
from collections import deque

read = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(read())):
    rows, cols, lines = map(int, read().split())
    grid = [[0] * cols for _ in range(rows)]
    # 배추 심기
    for _ in range(lines):
        x, y = map(int, read().split())
        grid[x][y] = 1

    answer = 0
    for row in range(rows):
        for col in range(cols):
            # 배추밭 발견
            if grid[row][col] == 1:
                # 지렁이 하나만 필요
                answer += 1
                # 배추밭을 BFS 탐색하며 0 세팅
                grid[row][col] = 0
                queue = deque([(row, col)])
                while queue:
                    curr_x, curr_y = queue.popleft()
                    for i in range(4):
                        nx = curr_x + dx[i]
                        ny = curr_y + dy[i]
                        # 또다른 배추밭 발견
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            queue.append((nx, ny))
    print(answer)
