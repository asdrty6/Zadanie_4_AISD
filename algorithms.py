def find_eulerian_cycle(graph):
    adj_matrix = [row[:] for row in graph.adj_matrix]
    num_vertices = graph.num_vertices
    
    if num_vertices == 0:
        return []

    curr_path = [0]
    circuit = []

    while curr_path:
        curr_v = curr_path[-1]
        has_edge = False
        
        for next_v in range(num_vertices):
            if adj_matrix[curr_v][next_v] == 1:
                adj_matrix[curr_v][next_v] = 0
                adj_matrix[next_v][curr_v] = 0
                curr_path.append(next_v)
                has_edge = True
                break
        
        if not has_edge:
            circuit.append(curr_path.pop())

    return circuit[::-1]


def find_hamiltonian_cycle(graph):
    num_vertices = graph.num_vertices
    path = [-1] * num_vertices
    path[0] = 0

    def is_safe(v, pos):
        if graph.adj_matrix[path[pos - 1]][v] == 0:
            return False
        for vertex in path:
            if vertex == v:
                return False
        return True

    def hamiltonian_util(pos):
        if pos == num_vertices:
            if graph.adj_matrix[path[pos - 1]][path[0]] == 1:
                return True
            return False

        for v in range(1, num_vertices):
            if is_safe(v, pos):
                path[pos] = v
                if hamiltonian_util(pos + 1):
                    return True
                path[pos] = -1
                
        return False

    if not hamiltonian_util(1):
        return []

    path.append(path[0])
    return path