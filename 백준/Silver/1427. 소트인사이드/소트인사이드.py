import sys

read = sys.stdin.readline

# 1. 문자열 의 각 문자 들을 리스트 각각 숫자로 저장 후 내림 차순 정렬
# 2. 리스트 언패킹 후 구분자 공백 으로 하여 출력 한다.
print(*sorted(map(int, read().rstrip()), reverse=True), sep='')
