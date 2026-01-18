import sys

read = sys.stdin.readline

stack = []
for _ in range(int(read())):
    n = int(read())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
if stack:
    print(sum(stack))
else:
    print('0')
