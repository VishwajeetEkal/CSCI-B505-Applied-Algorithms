def grandTour(connections):
    def is_valid(v, pos, p, marked):
        if connections[p[pos - 1]][v] == 0:
            return False
        if marked[v]:
            return False
        return True

    def hamiltonian_util(pos):
        if pos == num_vertices:
            return connections[p[pos - 1]][p[0]] == 1

        for v in range(1, num_vertices):
            if is_valid(v, pos, p, marked):
                p[pos] = v
                marked[v] = True

                if hamiltonian_util(pos + 1):
                    return True

                p[pos] = -1
                marked[v] = False

        return False

    num_vertices = len(connections)
    p = [-1] * num_vertices
    marked = [False] * num_vertices

    p[0] = 0
    marked[0] = True

    if not hamiltonian_util(1):
        return False

    if connections[p[num_vertices - 1]][p[0]] == 0:
        return False

    return True


# Example 1
checkpoints1 = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0]
]
print(grandTour(checkpoints1))  # Output: True

# Example 2
checkpoints2 = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0]
]
print(grandTour(checkpoints2))  # Output: False
