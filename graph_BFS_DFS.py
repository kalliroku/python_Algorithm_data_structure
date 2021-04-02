class Graph:
    def __init__(self, max_vertex_count, direct=0, array=0):
        self.max_vertex_count = max_vertex_count
        self.current_vertex_count = 0
        self.directed_graph = direct
        self.vertex_list = [0] * (max_vertex_count + 1)
        self.edge_matrix = []
        self.array_graph = array
        if self.array_graph == 0:
            for _ in range(self.max_vertex_count + 1):
                self.edge_matrix.append([])
        else:
            for _ in range(self.max_vertex_count + 1):
                self.edge_matrix.append([0] * (self.max_vertex_count+1))

    def is_full(self):
        return 1 if self.max_vertex_count <= self.current_vertex_count else 0

    def is_vertex_exist(self, vertex):
        return 1 if self.vertex_list[vertex] == 1 else 0

    def add_vertex(self, vertex):
        # if self.is_full():
        #     print("vertex storage is full")
        #     return 0
        # else:
        if self.vertex_list[vertex] == 1:
            return 0
        else:
            self.vertex_list[vertex] = 1
            self.current_vertex_count += 1
            return 1

    def add_edge(self, start_vertex, end_vertex, weight=1):
        if self.is_vertex_exist(start_vertex) and self.is_vertex_exist(end_vertex):
            if self.array_graph:
                self.edge_matrix[start_vertex][end_vertex] = weight
                if not self.directed_graph:
                    self.edge_matrix[end_vertex][start_vertex] = weight
            else:
                self.edge_matrix[start_vertex].append(end_vertex)
                if not self.directed_graph and start_vertex not in self.edge_matrix[end_vertex]:
                    self.edge_matrix[end_vertex].append(start_vertex)
        else: return 0

    def display_graph(self):
        print(self.__class__.__name__)
        if self.array_graph:
            for i in range(self.max_vertex_count + 1):
                for j in range(self.max_vertex_count + 1):
                    print(self.edge_matrix[i][j], "", end="")
                print()
        else:
            for i in self.edge_matrix:
                for j in i:
                    print(j, "", end="")
                print()

    def del_edge(self, start_vertex, end_vertex):
        if self.array_graph:
            self.edge_matrix[start_vertex][end_vertex] = 0
            if not self.directed_graph:
                self.edge_matrix[end_vertex][start_vertex] = 0
        else:
            self.edge_matrix[start_vertex].remove(end_vertex)
            if not self.directed_graph:
                self.edge_matrix[end_vertex].remove(start_vertex)

    def del_vertex(self, vertex):
        if self.is_vertex_exist(vertex):
            self.vertex_list[vertex] = 0
            self.current_vertex_count -= 1
            if self.array_graph:
                for i in self.edge_matrix[vertex]:
                    self.edge_matrix[vertex][i] = 0
                if not self.directed_graph:
                    for j in self.edge_matrix:
                        j[vertex] = 0
            else:
                self.edge_matrix[vertex] = []
                if not self.directed_graph:
                    for i in self.edge_matrix:
                        try:
                            i.remove(vertex)
                        except ValueError:
                            pass

    def clear_graph(self):
        self.__init__(self.max_vertex_count, self.directed_graph, self.array_graph)


import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
edge_list = list()
for _ in range(M):
    edge_list.append(list(map(int, sys.stdin.readline().split())))


def list_to_graph(graph, edge_list):
    for i in edge_list:
        x = i[0]
        y = i[1]
        graph.add_vertex(x)
        graph.add_vertex(y)
        graph.add_edge(x, y)
    for i in range(graph.max_vertex_count + 1):
        graph.edge_matrix[i] = list(set(graph.edge_matrix[i]))
        graph.edge_matrix[i].sort(reverse=True)
    # graph.display_graph()
    # print("-" * (graph.max_vertex_count + 1))


def dfs_graph(N, edge_list, start_vertex):
    # 무방향, 연결리스트 그래프
    graph = Graph(N)
    # 정점 및 간선 추가
    list_to_graph(graph, edge_list)
    # 스택 선언
    stack = list()
    # 방문 리스트 선언
    result = list()
    # 시작 위치 스택에 추가
    stack.append(start_vertex)
    # 시작 위치 방문 리스트 추가
    result.append(start_vertex)
    # 스택이 빌 때까지-(탐색 실패)
    while stack:
        # 스택을 팝 (현재 위치 설정)
        visiting_vertex = stack.pop()
        #  정점에 미방문 간선이 존재 하지 않으면 아래 진행
        while graph.edge_matrix[visiting_vertex]:
            # 방문 중인 위치가 방문 리스트에 없으면 추가
            if visiting_vertex not in result: result.append(visiting_vertex)
            #  방문이 가능한 간선이 나올 때 까지 for 반복 pop 진행
            for _ in range(len(graph.edge_matrix[visiting_vertex])):
                temp_vertex = graph.edge_matrix[visiting_vertex].pop()
                # 미방문 정점을 찾으면 현재 위치를 스택에 넣고 다음 정점 탐색을 위해 break
                if temp_vertex not in result:
                    stack.append(visiting_vertex)
                    visiting_vertex = temp_vertex
                    break
    return result


def bfs_graph(N, edge_list, start_vertex):
    graph = Graph(N)
    list_to_graph(graph, edge_list)
    queue = deque()
    result = list()
    # 큐와 방문 리스트에 시작 정점 추가
    queue.append(start_vertex)
    result.append(start_vertex)
    while queue:
        # 큐에서 디큐하여 탐색 위치 설정
        visiting_vertex = queue.popleft()
        # 현재 위치가 미방문 위치면 방문 리스트에 추가
        if visiting_vertex not in result: result.append(visiting_vertex)
        # 현재 위치의 방문 가능 위치 중 미방문 지점을 모두 인큐
        for _ in range(len(graph.edge_matrix[visiting_vertex])):
            temp_vertex = graph.edge_matrix[visiting_vertex].pop()
            if temp_vertex not in result:
                queue.append(temp_vertex)
        # 현 위치(정점)의 방문 가능 정점을 모두 인큐 후에는 while문으로 돌아가 디큐로 다음 정점 탐색 시작
    return result


print(" ".join(map(str, dfs_graph(N, edge_list, V))))
print(" ".join(map(str, bfs_graph(N, edge_list, V))))
