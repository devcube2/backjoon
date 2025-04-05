import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for row in graph:
    row.sort()


def DFS(now):
    print(now, end=" ")
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            DFS(next)


def BFS(start):
    visited[start] = True
    que = [start]

    while que:
        now = que.pop(0)
        print(now, end=" ")
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                que.append(next)


DFS(now=v)
print()
visited = [False for _ in range(n+1)]
BFS(start=v)