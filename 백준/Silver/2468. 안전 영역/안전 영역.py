import sys, copy
from collections import deque

read = sys.stdin.readline


# 비에 잠기지 않은 안전 지역을 비로 채운다.
def rainy_walk(land, x, y):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 지도 범위를 벗어 났다면
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            # 안전 영역에 해당 한다면
            if land[ny][nx] == 1:
                land[ny][nx] = 0
                queue.append((ny, nx))


land = [list(map(int, read().split())) for _ in range(int(read()))]
# N: 행, M: 열
N, M = len(land), len(land[0])

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 땅을 가득 채울 수 있는 비의 양 구하기
rain_max = max(num for row in land for num in row)

safe_area = []
# 비가 안오는 경우 부터 최대로 올 수 있는 비의 양까지 루프를 돌면서 안전 영역을 구한다.
for rain in range(0, rain_max + 1):
    # 안전 지역 개수
    safe_area_count = 0
    # 비에 잠긴 땅 구하기
    rainy_land = [[1 if n > rain else 0 for n in row] for row in land]
    # 비에 잠긴 땅의 모든 타일 돌면서 안전 지역 개수 구하기
    for y in range(M):
        for x in range(N):
            if rainy_land[y][x] == 1:
                rainy_walk(rainy_land, x, y)
                safe_area_count += 1
    safe_area.append(safe_area_count)

print(max(safe_area))
