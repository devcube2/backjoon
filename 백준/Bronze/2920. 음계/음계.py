import sys

read = sys.stdin.readline

asc = [n for n in range(1, 9)]
desc = [n for n in range(8, 0, -1)]

nums = list(map(int, read().split()))
if asc == nums:
    print('ascending')
elif desc == nums:
    print('descending')
else:
    print('mixed')
