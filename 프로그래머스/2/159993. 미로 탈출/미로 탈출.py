from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
pass_blocks = "OSLE"

# start 에서 exit 를 발견하기까지 거리 리턴
def compute_path_length(maps, start, exit):    
    rows, cols = len(maps), len(maps[0])
    
    visited = [[False] * cols for _ in range(rows)]
    distance = [[0] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    queue = deque([start])
    while queue:
        curr_x, curr_y = queue.popleft()
        
        # exit 발견
        if maps[curr_x][curr_y] == maps[exit[0]][exit[1]]:
            return distance[curr_x][curr_y]        
        
        # 4방향 탐색
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            # 맵 범위 & 패스블록 & 방문 확인
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] in pass_blocks and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[curr_x][curr_y] + 1
                queue.append((nx, ny))
    return -1

def solution(maps):
    # start, exit, lever 위치 저장
    start = exit = lever = (0, 0)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            ch = maps[i][j]
            if ch == 'S':
                start = (i, j)
            elif ch == 'L':
                lever = (i, j)
            elif ch == 'E':
                exit = (i, j)
    
    # start -> lever 거리
    answer = 0
    path_length = compute_path_length(maps, start, lever)
    if path_length > 0:
        answer += path_length
    else:
        return -1    
    
    # lever -> exit 거리
    path_length = compute_path_length(maps, lever, exit)
    if path_length > 0:
        answer += path_length
    else:
        return -1
    
    return answer