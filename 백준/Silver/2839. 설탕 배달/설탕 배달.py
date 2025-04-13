import sys

read = sys.stdin.readline

N = int(read())

answer = 0
while N >= 0:
    # 5kg 로 처리 가능한 지 확인
    if N % 5 == 0:
        # 5kg 봉지수 더함
        answer += N // 5
        print(answer)
        break
    # 3kg 빼고, 1봉지 더함
    N -= 3
    answer += 1
else:
    print(-1)
