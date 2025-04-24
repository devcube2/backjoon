import sys

read = sys.stdin.readline

money = int(read())

answer = 0
while money >= 0:
    # 5원 동전 으로 딱 떨어 지는지 확인
    if money % 5 == 0:
        answer += money // 5
        print(answer)
        break
    # 5원 으로 마무리 안되니, 2원 하나 뺀다
    money -= 2
    answer += 1
else: # 거스름 불가능
    print(-1)
