import sys, copy
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())

paper = [[int(c) for c in read().split()] for _ in range(n)]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]


# 탐색 하면서 색칠된 부분을 발견 하면 지우고 리턴 값에 1을 더한다. 리턴 값은 그림의 크기가 된다.
def paint(x, y):
    count = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for direction in range(5):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 범위 유효한 지 체크
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            # 색칠된 부분 이라면
            if paper[ny][nx] == 1:
                count += 1
                paper[ny][nx] = 0
                queue.append((nx, ny))
    return count


pictures = []
# 모든 타일에 대해서 검사 한다.
for y in range(n):
    for x in range(m):
        if paper[y][x] == 1:
            count = paint(x, y)
            if count > 0:
                pictures.append(count)

print(len(pictures))
print(max(pictures) if pictures else 0)
