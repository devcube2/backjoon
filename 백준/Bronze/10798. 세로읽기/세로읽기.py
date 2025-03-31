import sys

read = sys.stdin.readline

rows = 5
words = []
for _ in range(rows):
    word = list(read().rstrip())
    word.extend([' '] * (15 - len(word))) # 없는 부분 공백 채우기
    words.append(word)

answer = [words[j][i] for i in range(15) for j in range(rows)] # 세로 읽기
answer = ''.join(answer).replace(' ', '') # 공백 제거
print(answer)
