import itertools
import sys

read = sys.stdin.readline

# 색종이 수
N = int(read())

# 100 * 100 도화지 만들기
paper = [[0] * 100 for _ in range(100)]

# 색종이 수만큼 루프 돌면서 색칠 한다.
for _ in range(N):
    # 색종이 붙이는 시작 좌표
    x_start, y_start = map(int, read().split())
    # index 0 부터 시작 이므로 1씩 빼준다.
    x_start -= 1
    y_start -= 1
    # 10 * 10 범위 만큼 색칠 하기
    for y in range(10):
        for x in range(10):
            paper[y_start + y][x_start + x] = 1

# list in list 를 평탄화 하고 sum 구해서 출력
print(sum(list(itertools.chain.from_iterable(paper))))
