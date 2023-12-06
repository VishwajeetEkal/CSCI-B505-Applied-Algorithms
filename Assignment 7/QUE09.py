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

def WeightLimitedPathsExist(n, edgelist, querylist):
    
    edgelist.sort(key=lambda x: x[2], reverse=True)

    weightedLimitedPath = []

    for query in querylist:
        p, q, w = query
        ancestor = [i for i in range(n)]
        rank = [0] * n

        for edge in edgelist:
            u, v, wt = edge
            root_u = findAncestor(ancestor, u)
            root_v = findAncestor(ancestor, v)

            if wt >= w:
                unionAncestor(ancestor, rank, root_u, root_v)

            if findAncestor(ancestor, p) == findAncestor(ancestor, q):
                weightedLimitedPath.append(True)
                break

        else:
            weightedLimitedPath.append(False)

    return weightedLimitedPath


n = 6
edges = [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]
queries = [[2, 3, 1], [1, 3, 3], [2, 0, 3], [0, 5, 6]]

output = WeightLimitedPathsExist(n, edges, queries)
print(output)  


print(WeightLimitedPathsExist(6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]], [[2, 3, 2], [1, 3, 3], [2, 0, 3], [0, 5, 6]]))
print(WeightLimitedPathsExist(3, [[0, 1, 4], [0, 1, 2], [1, 2, 3]], [[0, 2, 3], [0, 2, 6]]))
