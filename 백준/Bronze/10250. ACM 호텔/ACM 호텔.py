import sys

read = sys.stdin.readline

for _ in range(int(read())):
    H, W, N = map(int, read().split())
    q, r = divmod(N, H)
    if H == 1:
        print(f"{H}{N:02d}")
    elif r == 0:
        print(f"{H}{r + (N // H):02d}")
    else:
        print(f"{r}{q + 1:02d}")
