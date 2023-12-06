import copy
from typing import List
import heapq

def specialHub(n, edges, distanceThreshold):
    
    distanceAdjMatrix = [[float('inf')] * n for _ in range(n)]
    
    for pathway in edges:
        startCity, endCity, weight = pathway
        distanceAdjMatrix[endCity][startCity] = weight
        distanceAdjMatrix[startCity][endCity] = weight    

    itrk = 0
    while itrk < n:
        itri = 0
        while itri < n:
            itrj = 0
            while itrj < n:
                if itri != itrj:
                    distanceAdjMatrix[itri][itrj] = min(distanceAdjMatrix[itri][itrk] + distanceAdjMatrix[itrk][itrj], distanceAdjMatrix[itri][itrj])
                itrj += 1
            itri += 1
        itrk += 1

    minReach = float('inf')
    answer = -1
    
    itr = 0
    while itr < n:
        citiesWithinLim = sum(1 for d in distanceAdjMatrix[itr] if d <= distanceThreshold)

        if citiesWithinLim <= minReach or ( itr > answer and citiesWithinLim == minReach):
            minReach = citiesWithinLim
            answer = itr
        
        itr += 1

    return answer

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

def cheapestRoutes(s, prices):
    lenPrices = len(prices)
    
    minPrices = [-1] * lenPrices
    
    visitQue = [(0, s)]

    while visitQue:
        priceToTravel, currentCity = heapq.heappop(visitQue)

        if minPrices[currentCity] != -1 and priceToTravel > minPrices[currentCity]:
            continue

        minPrices[currentCity] = priceToTravel

        for neighborCity, ticketPrice in enumerate(prices[currentCity]):
            if ticketPrice != -1:

                totalPrice = priceToTravel + ticketPrice

                if totalPrice < minPrices[neighborCity] or minPrices[neighborCity] == -1:
                    heapq.heappush(visitQue, (totalPrice, neighborCity))

    return minPrices

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


def findMaxSuccessPath(n, edges, prob, start_node, end_node):
    edgeList = {itr: [] for itr in range(n)}

    for comLink, p in zip(edges, prob):
        a, b = comLink
        edgeList[a].append((b, p))
        edgeList[b].append((a, p)) 

    visitQue = [(-1, start_node)]

    maximumProb = {itr: 0 for itr in range(n)}
    maximumProb[start_node] = 1

    while visitQue:
        currentProbability, curVert = heapq.heappop(visitQue)

        currentProbability = -currentProbability
  
        if currentProbability < maximumProb[curVert]:
            continue

        for neigVert, neigVert_prob in edgeList[curVert]:
            newProbability = currentProbability * neigVert_prob

            if newProbability > maximumProb[neigVert]:
                maximumProb[neigVert] = newProbability
                heapq.heappush(visitQue, (-newProbability, neigVert))
  
    return maximumProb[end_node]

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



def manDist(hubOne, hubTwo):
        return abs(hubOne[0] - hubTwo[0]) + abs(hubOne[1] - hubTwo[1])

def minCostToConnectHubs(hubs):
    visitQue = [(0, tuple(hubs[0]))]  
    
    visited = set()
    
    totalCost = 0

    while visitQue:
        cost, currentHub = heapq.heappop(visitQue)

        if currentHub in visited:
            continue
        
        visited.add(currentHub)

        totalCost += cost
      
        for neighborHub in hubs:
            neighborHubTuple = tuple(neighborHub)
            if neighborHubTuple not in visited:
                heapq.heappush(visitQue, (manDist(neighborHubTuple, currentHub), neighborHubTuple))

    return totalCost

def minimumTimeToVisit(grid):
    rowLen, colLen = len(grid), len(grid[0])

    visitQue = [(grid[0][0], 0, 0)]

    while visitQue:
        
        timeToTravel, row, col = heapq.heappop(visitQue)
    
        validDir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for dr, dc in validDir:
            newRow, newCol = row + dr, col + dc

            if newRow == rowLen-1 and newCol == colLen-1:
                return timeToTravel+1
    
            if 0 <= newRow < rowLen and 0 <= newCol < colLen and grid[newRow][newCol] <=timeToTravel+1:
                if (timeToTravel + 1, newRow, newCol) not in visitQue:
                    heapq.heappush(visitQue, (timeToTravel + 1, newRow, newCol))

    
    return -1

def shortestFareRoute(start, target, specialRoads):

    manCost = manDist(start,target)

    fareEdgeList = {}
    for road in specialRoads:
        u = (road[0], road[1])
        v = (road[2], road[3])
        fareReq = road[-1]

        if u not in fareEdgeList:
            fareEdgeList[u] = []
        fareEdgeList[u].append((v, fareReq))

        if v not in fareEdgeList:
            fareEdgeList[v] = []
        fareEdgeList[v].append((u, fareReq))

    
    if tuple(start) not in list(fareEdgeList.keys()):
        temp3 = float('inf')
        for new_start in list(fareEdgeList.keys()):
            
            (c,d) = new_start

            temp1 = shortestFareRoute([c,d], target, specialRoads) + manDist(start,[c,d]) 
            if temp1 < temp3:
                temp3 = temp1

        return manCost if manCost < temp3 else temp3
    

    heap = [(0, start)]
    visited = []
    fare, currentLoc = None,None
    bridgMan = float('inf')
    temp = 0

    while heap:
        
        fare, currentLoc = heapq.heappop(heap)

        temp = fare+ manDist(currentLoc, target)
        
        if temp <= bridgMan:
            bridgMan = temp

        if currentLoc == target:
            return fare

        
        if currentLoc in visited:
            continue

        visited.append(currentLoc)

        if tuple(currentLoc) in list(fareEdgeList.keys()):
            for neighLoc, fareReq in fareEdgeList[tuple(currentLoc)]:
                if neighLoc not in visited:
                    heapq.heappush(heap, (fare + fareReq, neighLoc))
    
    return manCost if manCost < bridgMan else bridgMan



