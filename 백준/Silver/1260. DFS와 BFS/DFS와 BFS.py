import sys
from collections import deque, defaultdict

read = sys.stdin.readline

# N: 정점의 개수, M: 간선의 개수, V: 시작할 정점 번호
N, M, V = map(int, read().split())

# 입력값 기반 그래프 생성
graph = defaultdict(list)
for _ in range(M):
    v1, v2 = map(int, read().split())
    # 양방향 이니까 반대도 입력
    graph[v1].append(v2)
    graph[v2].append(v1)

# (단, 방문할 수 있는 정점이 여러 개인 경우 에는 정점 번호가 작은 것을 먼저 방문) <-- 이 조건 만족을 위한 정렬
dfs_graph = {key: sorted(value, reverse=True) for key, value in graph.items()}
bfs_graph = {key: sorted(value) for key, value in graph.items()}

def dfs(graph, start):
    visit, visited, result = deque([start]), set(), []

    while visit:
        node = visit.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            visit.extend(
                graph.get(node, []))  # 정점만 있고 간선이 없는 경우 KeyError 방지, 그냥 graph[node] 를 하면 value 가 없어서 KeyError 발생
    return result

def bfs(graph, start):
    visit, visited, result = deque([start]), set(), []

    while visit:
        node = visit.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            visit.extend(graph.get(node, [])) # 정점만 있고 간선이 없는 경우 KeyError 방지, 그냥 graph[node] 를 하면 value 가 없어서 KeyError 발생
    return result

print(*dfs(dfs_graph, V))
print(*bfs(bfs_graph, V))
