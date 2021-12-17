"""
처음에 각 웜홀의 시작점에 대해(사이클은 반드시 웜홀을 포함할것이므로) 벨만-포드 알고리즘을 시행했었는데 시간초과가 떴다.
잘 생각해보니 이 문제에선 최단거리를 구할 필요가 없기 때문에 임의로 시작점 하나를 정해서
음수 사이클이 존재하는지만 확인해줬더니 제한시간 내에 통과 할 수 있었다.
"""
# 메모리 : 29708 KB
# 시간 : 2048 ms
import sys


def bellman_ford():
    # T는 최대 10000이므로 10001로 초기화 하였다.
    dist = [10001] * (N + 1)
    # 시작점을 정함. 최단거리가 아닌 음수 사이클의 유무를 확인할 것이기 때문에 아무곳(1~N)이나 정해도 됨.
    dist[1] = 0
    for i in range(N):
        # 모든 간선 확인
        for edge in edges:
            cur_node = edge[0]
            next_node = edge[1]
            time = edge[2]
            # 최단거리를 갱신 할 수 있다면 갱신
            if dist[next_node] > time + dist[cur_node]:
                dist[next_node] = time + dist[cur_node]
                # 만약 모든 반복 시행했는데도 갱신이 이루어졌다면, 음의 사이클이 존재하는것이다.
                if i == N - 1:
                    return True
    return False


s_input = sys.stdin.readline
# 테스트를 시행할 횟수
TC = int(s_input())

for _ in range(TC):
    # N: 정점 개수, M: 양수 간선(도로), W: 음수 간선(웜홀)
    N, M, W = map(int, s_input().split())
    # 간선의 정보를 저장할 배열
    edges = []

    # 도로 간선 추가
    for _ in range(M):
        S, E, T = map(int, s_input().split())
        edges.append((S, E, T))
        # 도로는 방향이 없으므로
        edges.append((E, S, T))
    # 웜홀 간선 추가
    for _ in range(W):
        S, E, T = map(int, s_input().split())
        edges.append((S, E, -T))

    if bellman_ford():
        print("YES")
    else:
        print("NO")
