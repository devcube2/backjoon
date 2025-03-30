import sys

read = sys.stdin.readline

# 문자열 각 문자가 사용된 인덱스 위치들 저장
def index_characters(s):
    index_dict = {}
    for i, char in enumerate(s):
        if char in index_dict:
            index_dict[char].append(i)
        else:
            index_dict[char] = [i]
    return index_dict

# 순차 구성 확인
def is_seq(seq_list):
    if len(seq_list) == 1:
        return True
    for i in range(1, len(seq_list)):
        if seq_list[i - 1] + 1 != seq_list[i]:
            return False
    return True

answer = 0
for _ in range(int(read())):
    dic = index_characters(read().rstrip())
    flag = True
    for value in dic.values():
        if not is_seq(value): # 순차 구성이 아니라면
            flag = False
            break
    if flag:
        answer += 1
print(answer)
