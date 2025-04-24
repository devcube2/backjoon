import sys

read = sys.stdin.readline

for _ in range(int(read())):
    for word in read().strip().split():
        print(word[::-1], end=' ')
