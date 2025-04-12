import sys

read = sys.stdin.readline

N, M = map(int, read().split())

no_hear = {read().strip() for s in range(N)}
no_see = {read().strip() for s in range(M)}
no_hear_no_see = no_hear & no_see

print(len(no_hear_no_see))
for s in sorted(no_hear_no_see):
    print(s)
    