# Representing graphs with dictionaries

G = {'A': [], 'B': ['A', 'C'], 'C': ['A'], 'D': ['B']}


# Hamiltonian path

def hampath(graph):
    """Returns whether or not a Hamiltonian path exists in graph."""
    for vertex in graph:
        if hamiltonian(graph, vertex):
            return True
    return False

def hamiltonian(graph, vertex):
    """Returns whether or not a Hamiltonian path exists in graph
    starting from vertex.
    """
    def hamil_helper(v, visited):
        """Returns whether or not there is the rest of a Hamiltonian
        path starting from v, given the set of vertices already visited.
        """
        if v in visited:
            return False
        visited.add(v)
        if visited == set(graph):
            return True
        for next_v in graph[v]:
            if hamil_helper(next_v, visited):
                return True
        return False
    return hamil_helper(vertex, set())
