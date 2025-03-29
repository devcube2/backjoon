import sys
from collections import Counter

read = sys.stdin.readline

counter = Counter(read().rstrip().lower())

most = counter.most_common(2)
if len(most) == 1:
    print(most[0][0].upper())
elif most[0][1] == most[1][1]: # 최대 개수가 서로 같으면
    print('?')
else:
    print(most[0][0].upper())
