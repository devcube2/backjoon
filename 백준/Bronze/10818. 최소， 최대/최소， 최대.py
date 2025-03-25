import sys

read = sys.stdin.readline

read()
lst = [int(n) for n in read().split()]
print(min(lst), max(lst))
