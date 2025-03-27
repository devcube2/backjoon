import sys, string

read = sys.stdin.readline

for _ in range(int(read())):
    R, S = read().split()
    a = [c * int(R) for c in S]
    print(''.join([c * int(R) for c in S]))
