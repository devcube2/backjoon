import sys

read = sys.stdin.readline

N, X = map(int, read().split())
lst = [n for n in read().split() if int(n) < X]
print(' '.join(lst))
