import sys

line = sys.stdin.readline()

in_list = [int(n) for n in line.split()]
piece_count = [1, 1, 2, 2, 2, 8]

print(*[y - x for x, y in zip(in_list, piece_count)])
