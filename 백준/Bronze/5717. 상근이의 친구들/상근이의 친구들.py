import sys

read = sys.stdin.readline

while True:
    M, N = map(int, read().split())
    if M == 0 and N == 0:
        break
    print(M+N)
