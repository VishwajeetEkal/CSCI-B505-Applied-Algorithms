def findAncestor(ancestor, succ):
    if ancestor[succ] != succ:
        ancestor[succ] = findAncestor(ancestor, ancestor[succ])
    return ancestor[succ]

def unionAncestor(ancestor, rank, x, y):
    rootX = findAncestor(ancestor, x)
    rootY = findAncestor(ancestor, y)

    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            rootX, rootY = rootY, rootX
        ancestor[rootY] = rootX
        if rank[rootX] == rank[rootY]:
            rank[rootX] += 1

def min_cost_to_supply_water(n, wells, pipes):
    edgeList = []
    for inumWells, price in enumerate(wells):
        edgeList.append((0, inumWells + 1, price))  

    for pipe in pipes:
        edgeList.append((pipe[0], pipe[1], pipe[2]))

    edgeList.sort(key=lambda x: x[2])  

    ancestor = [i for i in range(n + 1)] 
    rank = [0] * (n + 1)

    minPrice = 0
    indexEl = 0

    while indexEl < len(edgeList):
        u, v, price = edgeList[indexEl]
        if findAncestor(ancestor, u) != findAncestor(ancestor, v):
            unionAncestor(ancestor, rank, u, v)
            minPrice += price
        indexEl += 1

    return minPrice


n1 = 3
wells1 = [1, 2, 2]
pipes1 = [[1, 2, 1], [2, 3, 1]]
print(min_cost_to_supply_water(n1, wells1, pipes1))  # Output: 3


n2 = 2
wells2 = [1, 1]
pipes2 = [[1, 2, 1], [1, 2, 2]]
print(min_cost_to_supply_water(n2, wells2, pipes2))  # Output: 2
