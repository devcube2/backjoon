import sys

read = sys.stdin.readline

for _ in range(int(read())):
    s = read().rstrip()
    print(s[0] + s[-1])
