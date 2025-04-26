import sys, re

read = sys.stdin.readline

S = read().strip()
K = read().strip()

# 숫자 제거
S = re.sub(r'[0-9]', '', S)
# 부분 문자열 인지 체크 후 출력 
print(1 if K in S else 0)
