import sys
from collections import Counter

read = sys.stdin.readline

counter = Counter(str(int(read()) * int(read()) * int(read())))
for n in range(10):
    print(counter[str(n)])
