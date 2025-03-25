import sys

read = sys.stdin.readline

N, M = map(int, read().split())

answer = [0] * N
for _ in range(M):
    i, j, k = map(int, read().split())
    answer[i-1 : j] = [k] * (j-i+1)
print(*answer)
