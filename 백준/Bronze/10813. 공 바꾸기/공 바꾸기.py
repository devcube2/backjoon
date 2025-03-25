import sys

read = sys.stdin.readline

N, M = map(int, read().split())

answer = [n for n in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, read().split())
    answer[i-1], answer[j-1] = answer[j-1], answer[i-1]
print(*answer)
