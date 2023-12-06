import copy
from typing import List

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

def challenge(n, connections):

    ancestor = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    connections = copy.deepcopy(connections)
    connections.sort(key=lambda x: x[2])

    totalCost, edgeCount = 0,0

    for connection in connections:
        x, y, cost = connection
        rootX = findAncestor(ancestor, x)
        rootY = findAncestor(ancestor, y)


        if rootX != rootY:
            totalCost += cost
            edgeCount += 1
            unionAncestor(ancestor, rank, rootX, rootY)


    return totalCost if edgeCount == n - 1 else -1


print(challenge(3, [[1,2,5],[1,3,6],[2,3,1]]))  # Output: 6


print(challenge(4, [[1,2,3],[3,4,4]]))  # Output: -1
