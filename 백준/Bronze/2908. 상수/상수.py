import sys

read = sys.stdin.readline

answer = [int(s[::-1]) for s in read().split()]

print(max(answer))
