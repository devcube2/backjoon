import sys

read = sys.stdin.readline

print(len({int(read()) % 42 for _ in range(10)}))
