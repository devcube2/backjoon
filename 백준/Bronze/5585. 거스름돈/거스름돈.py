import sys

read = sys.stdin.readline

answer = 0
money = 1000 - int(read())

# 가장 큰단위 잔돈 부터 계산
for n in [500, 100, 50, 10, 5, 1]:
    # 잔돈 개수 더하기
    answer += money // n
    # 잔액 에서 잔돈 빼기 
    money %= n
print(answer)
