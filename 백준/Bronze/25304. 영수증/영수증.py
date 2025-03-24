import sys

read = sys.stdin.readline

fee = int(read())

prices = [n * m for n, m in (tuple(map(int, read().split())) for _ in range(int(read())))]

print("Yes" if fee == sum(prices) else "No")
