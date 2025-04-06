import sys

read = sys.stdin.readline

dan_ji_map = [[int(c) for c in read().rstrip()] for _ in range(int(read()))]

# 제자리,동,서,남,북
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

x_max = len(dan_ji_map[0])
y_max = len(dan_ji_map)


# 한 단지를 걸으며 집의 수를 조사 한다.
def walk(x, y):
    visit = [(x, y)]    

    result = 0
    while visit:
        x, y = visit.pop()  # 현재 좌표값 얻기
        for direction in range(5):  # 네방향 이동
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < x_max and 0 <= ny < y_max and dan_ji_map[ny][nx] == 1:  # 좌표가 지도 내에 있고, 집이 존재 하면
                dan_ji_map[ny][nx] = 0  # 다시 세지 않기 위해서 0으로 만든다. visited 를 사용 하지 않는다.
                result += 1  # 집의 수 하나 증가
                visit.append((nx, ny))  # 다음 탐색 타일 추가
    return result  # 탐색 완료된 한 단지의 집의 수 리턴


answer = []
# 지도내 모든 타일을 조사 한다.
for x in range(x_max):
    for y in range(y_max):
        if dan_ji_map[y][x] == 1:
            answer.append(walk(x, y))  # 조사 결과 추가

answer.sort()  # 결과 오름 차순 정렬
print(len(answer))  # 총 단지 수 출력
for n in answer:
    print(n)  # 단지에 속하는 집의 수 출력
