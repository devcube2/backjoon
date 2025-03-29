import sys, re

read = sys.stdin.readline

line = read().rstrip()
patterns = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

answer = 0
for pattern in patterns:
    line, count = re.subn(pattern, " ", line) # 문자가 합쳐지지 않도록 공백 넣기
    answer += count
line = line.replace(" ", "") # 공백 제거
print(answer + len(line)) # 제거후 문자수 더해서 출력
