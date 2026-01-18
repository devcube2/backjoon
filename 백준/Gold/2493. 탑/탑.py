import sys

read = sys.stdin.readline

read()
towers = list(map(int, read().split()))

stack = []
answer = [0] * len(towers)
for i, tower in enumerate(towers):
    while stack:
        # 현재 타워 비교
        if towers[stack[-1]] > tower:
            answer[i] = stack[-1] + 1
            break
        else:
            # 현재 타워보다 작은 타워 삭제(내림차순 유지)
            stack.pop()
    stack.append(i)
print(*answer)
