from collections import defaultdict


def solution(record):
    answer = []

    # 최종 닉네임 저장
    users = defaultdict()
    for s in record:
        if s.split()[0] == 'Leave':
            continue
        _, id, nick = s.split()
        users[id] = nick

    # 최종 닉네임 으로 record 작성
    for s in record:
        s_split = s.split()
        command = s_split[0]
        id = s_split[1]
        if command == 'Enter':
            answer.append(f'{users[id]}님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(f'{users[id]}님이 나갔습니다.')

    return answer