import sys
from collections import deque

read = sys.stdin.readline
N, K = map(int, read().split())

MAX = 100000
dist = [-1] * (MAX + 1)  # -1은 미방문, 0 이상의 값은 도달 시간
dist[N] = 0
queue = deque([N])

while queue:
    curr = queue.popleft()
    
    if curr == K:
        print(dist[curr])
        break
        
    for next_node in (curr - 1, curr + 1, curr * 2):
        if 0 <= next_node <= MAX and dist[next_node] == -1:
            dist[next_node] = dist[curr] + 1
            queue.append(next_node)