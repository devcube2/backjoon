import sys

read = sys.stdin.readline

A, B = map(int, read().split())
A -= 2
B -= 1
print(3 + (min(A, B) * 2))
