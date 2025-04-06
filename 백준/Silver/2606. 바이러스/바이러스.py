import sys
from collections import defaultdict

read = sys.stdin.readline

V = int(read())
E = int(read())

# 그래프 생성
graph = defaultdict(list)
for _ in range(E):
    v1, v2 = map(int, read().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(graph, start):
    visit, visited = [start], set()

    while visit:
        node = visit.pop()
        if node not in visited:
            visited.add(node)
            visit.extend(graph.get(node, []))

    return visited

# 1번 컴퓨터 제외 -1 해줌
print(len(dfs(graph, 1)) - 1)
