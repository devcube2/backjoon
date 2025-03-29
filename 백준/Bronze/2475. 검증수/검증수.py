import sys

read = sys.stdin.readline

print(sum([int(n) ** 2 for n in read().split()]) % 10)
