import sys
from collections import deque

read = sys.stdin.readline

N, K = map(int, read().split())

level = 0
visited = set()
queue = deque([(N, level)])
while queue:
    node, level = queue.popleft()
    if node == K:
        print(level)
        break

    for next_node in [node - 1, node + 1, node * 2]:
        if 0 <= next_node <= 100000 and next_node not in visited:
            queue.append((next_node, level + 1))
            visited.add(next_node)
