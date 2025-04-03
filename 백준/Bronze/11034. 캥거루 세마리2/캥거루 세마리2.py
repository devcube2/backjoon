import sys

read = sys.stdin.readline

for line in sys.stdin:
    A, B, C = map(int, line.split())
    print(max(B-A, C-B)-1) # B 를 기준으로 더 큰 차이가 있는 값이 답이다.
