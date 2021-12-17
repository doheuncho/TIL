"""
방문 노드를 기록하는 visited를 방문한 노드의 알파벳으로 이루어진 set으로 구성했을경우 시간초과 발생.
오늘 배운 ASCII 코드를 이용한 list로 visited 수정.
내장함수 ord()는 지정된 문자의 ASCII 코드를 반환한다. ord('A') = 65다.
입력을 그냥 받을 경우, 개행을 의미하는 10값이 Board에 추가되어 rstrip()으로 개행을 제거했다.
=> pypy만 통과.
혹시 탐색이 모든 경로를 파악하기 때문인가 해서 max_len을 통해 가능한 최대길이에 도달하면 탐색을 종료시켰는데,
이번엔 pypy마저 시간초과가 발생하였다.(?)
찾아보니 DFS를 함수로 정의하는 대신 일반 반복문으로 처리하면 빨라진다고는 하는데 가독성이 떨어질것 같아 여기서 만족하려한다.
"""
# 메모리 : 181408 KB
# 시간 : 7148 ms
import sys


s_input = sys.stdin.readline

max_len = 0
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y, count):
    global max_len
    max_len = max(max_len, count)
    for d in di:
        nx = x + d[0]
        ny = y + d[1]
        if C > ny >= 0 and R > nx >= 0:
            a = Board[nx][ny]
            if visited[a] == 0:
                visited[a] = 1
                dfs(nx, ny, count+1)
                visited[a] = 0


visited = [0] * 26
R, C = map(int, s_input().split())
Board = []
for _ in range(R):
    line = list(map(lambda x: ord(x) - 65, s_input().rstrip()))
    Board.append(line)

visited[Board[0][0]] = 1
dfs(0, 0, 1)

print(max_len)
