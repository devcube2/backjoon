import sys

read = sys.stdin.readline

N, M = map(int, read().split())

answer = [n+1 for n in range(N)]
for _ in range(M):
    i, j = map(int, read().split())
    answer[i-1:j] = answer[i-1:j][::-1]
print(*answer)
