import sys

read = sys.stdin.readline

while True:
    a, b = map(int, read().split())
    if a == b == 0:
        break
    print(a + b)