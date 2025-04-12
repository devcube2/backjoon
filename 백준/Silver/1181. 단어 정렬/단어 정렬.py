import sys, copy

read = sys.stdin.readline

# 단어 중복 제거
words = {read().rstrip() for _ in range(int(read()))}

# 길이 정렬 후 길이 같으면 사전 정렬하여 출력
for s in sorted(words, key=lambda x: (len(x), x)):
    print(s)
