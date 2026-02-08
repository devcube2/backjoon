import sys, math

read = sys.stdin.readline

A, B, V = map(int, read().split())

print(math.ceil((V - B) / (A - B)))
