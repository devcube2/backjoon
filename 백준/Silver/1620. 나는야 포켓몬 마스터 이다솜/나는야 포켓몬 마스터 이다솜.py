import sys

input = sys.stdin.readline

i, j = map(int, input().split())

word_list = [input().rstrip() for _ in range(i)]
word_dict = {v: i + 1 for i, v in enumerate(word_list)}

for _ in range(j):
    v = input().rstrip()

    if v.isdigit():
        print(word_list[int(v) - 1])
    else:
        print(word_dict[v])