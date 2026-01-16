import sys

read = sys.stdin.readline

n = int(read())

stack = []
for _ in range(n):
    line = read().split()
    if line[0] == 'push':
        stack.append(line[1])
    elif line[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print("-1")
    elif line[0] == 'empty':
        print(int(len(stack) == 0))
