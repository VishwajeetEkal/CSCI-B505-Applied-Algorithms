from collections import defaultdict

def isDividePossible(n, connected_houses):
    conHouseGraph = defaultdict(list)

    for houseLink in connected_houses:
        u, v = houseLink
        conHouseGraph[u].append(v)
        conHouseGraph[v].append(u)

    connectHouse = [-1] * n  

    def ifPossible(vertex, temp):
        connectHouse[vertex] = temp
        for neighbor in conHouseGraph[vertex]:
            if connectHouse[neighbor] == -1:
                if not ifPossible(neighbor, 1 - temp):
                    return False
            elif connectHouse[neighbor] == connectHouse[vertex]:
                return False
        return True

    itrColor = 0
    while itrColor < n:
        if connectHouse[itrColor] == -1 and not ifPossible(itrColor, 0):
            return False
        itrColor += 1

    return True


n1 = 3
connected_houses1 = [[0,1], [1,2], [2,0]]
print(isDividePossible(n1, connected_houses1))  


n2 = 3
connected_houses2 = [[0, 1], [1, 2]]
print(isDividePossible(n2, connected_houses2))  
