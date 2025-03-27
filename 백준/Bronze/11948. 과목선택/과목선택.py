import sys

read = sys.stdin.readline

scores = [int(read()) for _ in range(6)]
print(sum(scores[:4]) - min(scores[:4]) + max(scores[4:]))
