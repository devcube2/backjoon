import sys

read = sys.stdin.readline

N, M = map(int, read().split())

# N개의 문자열 집합 S
words = {read().strip() for _ in range(N)}

answer = 0
for _ in range(M):
    # 집합 포함 여부 검사
    if read().strip() in words:
        answer += 1
print(answer)
