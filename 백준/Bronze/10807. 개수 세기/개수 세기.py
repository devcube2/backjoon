import sys

read = sys.stdin.readline

int(read())
print(list(map(int, read().split())).count(int(read())))
