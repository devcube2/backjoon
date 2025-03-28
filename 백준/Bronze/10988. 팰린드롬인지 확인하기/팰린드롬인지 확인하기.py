import sys

line = sys.stdin.readline().rstrip()

print(1 if line == line[::-1] else 0)
