# floyd O(n3)

import sys
input = sys.stdin.readline
# n(vertex_count), m(edge_count)
n = int(input())
m = int(input())

# 그래프 초기화
INF = (1e9)
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

# 간선 입력값 그래프에 입력
for k in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c

# 3 중 for 문을 돌면서 간선 경유 도착 시간의 최소 값으로 업데이트
for r in range(n):
    for v in range(n):
        for s in range(n):
            if graph[v][r] + graph[r][s] < graph[v][s]:
                graph[v][s] = graph[v][r] + graph[r][s]

# 결과 확인
for i in graph:
    for j in i:
        print(j, " ", end="")
    print()
