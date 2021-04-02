# 미완성
class Graph:
    def __init__(self, max_vertex_count, direct=0, array=0):
        self.max_vertex_count = max_vertex_count
        self.current_vertex_count = 0
        self.directed_graph = direct
        self.vertex_list = [0] * (max_vertex_count + 1)
        self.edge_matrix = []
        self.array_graph = array
        if self.array_graph == 0:
            for i in range(self.max_vertex_count + 1):
                self.edge_matrix.append([i])
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
                if not self.directed_graph:
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
