import sys

read = sys.stdin.readline

K = int(read())
D1, D2 = map(int, read().split())
print(K ** 2 - ((D2 - D1) / 2) ** 2)
