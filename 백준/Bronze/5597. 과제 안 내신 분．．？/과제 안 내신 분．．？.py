import sys

read = sys.stdin.readline

dic = {int(read()): 0 for _ in range(28)}

answer = []
for n in range(1, 31):
    if n not in dic:
        answer.append(str(n))
print(answer[0])
print(answer[1])
