import sys, string

read = sys.stdin.readline

dic = {}
for n, c in enumerate(read().strip()):
    if c not in dic:
        dic[c] = n

answer = [dic[c] if c in dic else -1 for c in string.ascii_lowercase]
print(*answer)
