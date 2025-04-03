import sys

read = sys.stdin.readline

C, K, P = map(int, read().split())

answer = 0
for c in range(1, C + 1):
    answer += (K * c) + (P * c**2)
print(answer)
