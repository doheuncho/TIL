# 메모리 : 31924 KB
# 시간 : 556 ms
from collections import deque


def move_line(n, line):
    queue = deque([ele for ele in line if ele != 0])
    result = [0 for _ in range(n)]
    for i in range(n):
        if not queue:
            break
        result[i] = queue.popleft()
        if not queue:
            break
        if result[i] == queue[0]:
            result[i] += queue.popleft()

    return result


def move_matrix(n, matrix, direction):
    # direction : 시계 방향 회전 횟수 0(왼쪽) 1(아래쪽) 2(오른쪽) 3(위쪽)
    for _ in range(direction):
        # 시계 방향 90도 회전
        matrix = list(zip(*matrix[::-1]))
    return [move_line(n, line) for line in matrix]


def get_max(matrix):
    max_value = 0
    for line in matrix:
        max_value = max(max_value, max(line))
    return max_value


N = int(input())
M = [list(map(int, input().split())) for i in range(N)]

answer = 0
for x in range(4):
    for y in range(4):
        for z in range(4):
            for u in range(4):
                for v in range(4):
                    temp = M[:]
                    temp = move_matrix(N, temp, x)
                    temp = move_matrix(N, temp, y)
                    temp = move_matrix(N, temp, z)
                    temp = move_matrix(N, temp, u)
                    temp = move_matrix(N, temp, v)
                    answer = max(answer, get_max(temp))
print(answer)
