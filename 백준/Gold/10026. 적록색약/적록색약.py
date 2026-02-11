import sys
from collections import deque

read = sys.stdin.readline

rows = cols = int(read())

grid = [read().strip() for _ in range(rows)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grid, visited, blindnees):
    area = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                # 현재 컬러 지정
                color = grid[i][j]
                # 색맹이면 RG 를 같은 컬러로 한다.
                if (color == 'R' or color == 'G') and blindnees:
                    color = 'RG'
                visited[i][j] = True
                queue = deque([(i, j)])
                while queue:
                    curr_x, curr_y = queue.popleft()
                    # 네방향 탐색
                    for k in range(4):
                        nx = curr_x + dx[k]
                        ny = curr_y + dy[k]
                        # 범위 체크
                        if 0 <= nx < rows and 0 <= ny < cols:
                            # 컬러 및 방문 체크
                            if grid[nx][ny] in color and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                # 구역 탐색끝
                area += 1
    return area

# 일반인
visited = [[False] * cols for _ in range(rows)]
print(bfs(grid, visited, False))

# 색맹
visited = [[False] * cols for _ in range(rows)]
print(bfs(grid, visited, True))
