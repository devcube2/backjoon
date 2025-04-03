import sys

read = sys.stdin.readline

_, A, B = map(int, read().split())
if A < B:
    print('Bus')
elif A > B:
    print('Subway')
else:
    print('Anything')
