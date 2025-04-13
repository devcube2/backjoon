import sys
from itertools import combinations

read = sys.stdin.readline

_, blackjack = map(int, read().split())

# 카드 리스트 구하기
cards = [int(n) for n in read().split()]

answer = 0
# 카드 3장 조합들 순회
for n in combinations(cards, 3):
    # 카드 3장 합 구하기
    sum_n = sum(n)
    # blackjack 이면 루프 종료
    if sum_n == blackjack:
        answer = blackjack
        break
    # blackjack 보다 작고, answer 보다 크다면 answer 보다 blackjack 에 가까운 수이다.
    elif blackjack > sum_n > answer:
        answer = sum_n
print(answer)

