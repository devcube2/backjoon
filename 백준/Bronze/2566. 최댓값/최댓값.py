import sys

read = sys.stdin.readline

numbers = [int(n) for _ in range(9) for n in read().split()]
print(max(numbers))
q, r = divmod(numbers.index(max(numbers)), 9)
print(q + 1, r + 1)
