import sys

read = sys.stdin.readline

for i in range(int(read())):
    print(f"{i+1}. {read().rstrip()}")
