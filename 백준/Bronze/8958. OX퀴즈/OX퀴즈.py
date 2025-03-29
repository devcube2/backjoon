import sys

read = sys.stdin.readline

for _ in range(int(read())):
    score = 0
    count = 0
    for c in read().rstrip():
        if c == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
