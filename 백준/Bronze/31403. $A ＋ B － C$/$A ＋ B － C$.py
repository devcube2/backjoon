import sys, re

read = sys.stdin.readline

A = int(read())
B = int(read())
C = int(read())

print(A + B - C)
print(int(str(A) + str(B)) - C)
