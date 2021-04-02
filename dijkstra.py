# dijkstra

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
#  n = vertex_count, m = edge_count
n, m = map(int, input().split())
# 시작 위치 input
start = int(input())
# 그래프 생성
graph = [[] for i in range(n + 1)]
# 최단거리 리스트 작성
distance = [INF] * (n + 1)
# 방문 리스트 생성 및 초기화
visit = [0] * (n + 1)
#  그래프 초기화(연결리스트로 만들거라서 생략)
#  edge 추가
for _ in range(m):
    edge = list(map(int, input().split()))
    graph[edge[0]].append((edge[1], edge[2]))


def dijkstra(start):
    # 우선순위 큐 생성
    q = []
    # 시작 위치 튜플 푸쉬
    q.append((0, start))
    # 시작 위치 거리 초기화
    distance[start] = 0
    while q:
        # 큐의 가장 낮은 코스트의 정점과 간선 정보를 팝
        dist, now = heapq.heappop(q)
        # 현재 정점 방문처리
        visit[now] = 1
        # 팝한 노드의 거리 값이 기록 된 거리 값보다 크면 다음 노드를 팝
        if dist > distance[now]:
            continue
        # 그래프에 기록 된 현재 정점의 간선들을 검색하여 최소값 업데이트
        for v in graph[now]:
            # 최단 거리 간선(dist)에서 다음 정점 까지의 거리를 더한 값 = cost
            cost = dist + v[1]
            # 정점 경우 거리와 기존 알고 있는 거리의 비교
            if distance[v[0]] > cost:
                # 경유 거리가 작은 경우 기록 및 인큐
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

