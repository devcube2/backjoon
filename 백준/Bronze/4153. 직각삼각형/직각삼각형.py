import sys

read = sys.stdin.readline

while True:
    a, b, c = map(int, read().split())
    if a == 0:
        break
    if a ** 2 + b ** 2 == c ** 2:
        print('right')
    elif a ** 2 + c ** 2 == b ** 2:
        print('right')
    elif b ** 2 + c ** 2 == a ** 2:
        print('right')
    else:
        print('wrong')
