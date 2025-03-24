import sys

read = sys.stdin.readline

s = int(read())

for i in range(1, 10):
    print(f"{s} * {i} = {s * i}")
    