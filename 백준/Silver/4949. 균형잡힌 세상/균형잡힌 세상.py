import sys, re

read = sys.stdin.readline

while True:
    s = read().rstrip()
    if s[0] == '.':
        break
    # '()[]' 제외한 모든 문자 제거
    s = re.sub(r'[^()\[\]]', '', s)

    # 왼쪽 연산자 저장 리스트
    op_left = []
    for c in s:
        if c == '(' or c == '[':
            op_left.append(c)
        elif c == ')':
            if not op_left or op_left.pop() != '(':
                break
        elif c == ']':
            if not op_left or op_left.pop() != '[':
                break
    else: # 루프 끝까지 순회 종료 시
        # 연산자 모두 매칭 됐는지 확인
        if not op_left:
            print('yes')
            continue
    # 중간에(break) 나온 경우
    print('no')
