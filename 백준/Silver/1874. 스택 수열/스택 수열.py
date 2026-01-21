import sys

read = sys.stdin.readline

seq = []
for _ in range(int(read())):
    seq.append(int(read()))

answer = []
stack = []

append_number = 0
for n in seq:
    if append_number < n:
        while append_number < n:
            append_number += 1
            stack.append(append_number)
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        if not stack:
            print('NO')
            sys.exit(0)

        while stack.pop() != n:
            if not stack:
                print('NO')
                sys.exit(0)
        answer.append("-")

for s in answer:
    print(s)
