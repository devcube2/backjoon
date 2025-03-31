import sys

read = sys.stdin.readline

N, M = map(int, read().split())


def add_matrix(matrices):
    n = len(matrices[0]) # 행길이
    m = len(matrices[0][0]) # 열길이
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            # 각 행렬 같은 위치 값 더함
            row.append(matrices[0][i][j] + matrices[1][i][j])
        result.append(row)
    return result


matrices = []
for _ in range(2): # 행렬 2개 입력
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, read().split())))
    matrices.append(matrix)

answer = add_matrix(matrices)
for i in range(len(answer)):
    print(*answer[i])
