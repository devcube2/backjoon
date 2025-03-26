import sys
import statistics

read = sys.stdin.readline

read()

scores = list(map(int, read().split()))
M = max(scores)
answer = [n / M * 100 for n in scores]
print(statistics.mean(answer))
