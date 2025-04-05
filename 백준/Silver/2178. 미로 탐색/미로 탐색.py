import sys
from collections import deque

read = sys.stdin.readline

# N: 미로의 행, M: 미로의 열
N, M = map(int, read().split())

# y: 시작행 위치, x: 시작열 위치
def walk(x, y):
    # 미로 입력
    maze = [read().rstrip() for _ in range(N)]

    # 방문 체크 및 거리 기록용
    visited = [[0] * M for _ in range(N)]

    # 동,서,남,북 이동용
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    # 시작큐 생성
    queue = deque()
    queue.append((y, x))
    # 시작 지점은 거리 1
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()
        # 현재 좌표 에서 동,서,남,북 한칸씩 이동해 본다.
        for direction in range(4):
            ny = y + dy[direction]
            nx = x + dx[direction]
            # 이동한 좌표가 유효한 좌표 인지 확인
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == "1" and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1 # 해당 좌표 위치에 탐색 길이 1 증가 시켜서 기록
                queue.append((ny, nx)) # 이동 좌표 추가

    return visited

# 마지막 좌표 위치에 기록된 탐색 길이 출력
print(walk(0, 0)[N-1][M-1])
