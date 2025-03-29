import sys

line = sys.stdin.readline().rstrip()

N = int(line)
max_count = 2 * N - 1

star_count = 1
space_count = max_count // 2
direction = True

for _ in range(max_count):
    print(" " * space_count + "*" * star_count)
    if direction:
        space_count -= 1
        star_count += 2
    else:
        space_count += 1
        star_count -= 2

    if star_count == max_count:
        direction = False
