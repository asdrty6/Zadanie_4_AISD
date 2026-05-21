import random

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.edges_count = 0

    def add_edge(self, u: int, v: int):
        if self.adj_matrix[u][v] == 0 and u != v:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
            self.edges_count += 1

    def remove_edge(self, u: int, v: int):
        if self.adj_matrix[u][v] == 1:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
            self.edges_count -= 1

    def display(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))


def generate_hamiltonian_graph(nodes: int, saturation: int) -> Graph:
    graph = Graph(nodes)
    vertices = list(range(nodes))
    random.shuffle(vertices)

    for i in range(nodes):
        graph.add_edge(vertices[i], vertices[(i + 1) % nodes])

    max_edges = (nodes * (nodes - 1)) // 2
    target_edges = int(max_edges * (saturation / 100.0))

    while graph.edges_count < target_edges:
        v1, v2, v3 = random.sample(range(nodes), 3)
        if graph.adj_matrix[v1][v2] == 0 and graph.adj_matrix[v2][v3] == 0 and graph.adj_matrix[v3][v1] == 0:
            graph.add_edge(v1, v2)
            graph.add_edge(v2, v3)
            graph.add_edge(v3, v1)

    return graph


def generate_non_hamiltonian_graph(nodes: int) -> Graph:
    graph = generate_hamiltonian_graph(nodes, 50)
    isolated_vertex = random.randint(0, nodes - 1)
    
    for i in range(nodes):
        graph.remove_edge(isolated_vertex, i)
        
    return graph