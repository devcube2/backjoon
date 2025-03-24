import sys

read = sys.stdin.readline

n = int(read())

for i, j in zip(range(n - 1, -1, -1), range(1, n + 1)):
    print(' ' * i + '*' * j)
