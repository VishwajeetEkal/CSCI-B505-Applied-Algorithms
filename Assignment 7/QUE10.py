import heapq

def manDist(hubOne, hubTwo):
        return abs(hubOne[0] - hubTwo[0]) + abs(hubOne[1] - hubTwo[1])

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

# Example usage:
start1 = (2, 2)
end1 = (4, 4)
bridges1 = [[1, 1, 2, 2, 2], [2, 2, 4, 3, 1]]
print(shortestFareRoute(start1, end1, bridges1))  # Output: 2

start2 = (5, 5)
end2 = (10, 10)
bridges2 = [[3, 3, 4, 4, 5], [5, 5, 7, 5, 2], [7, 5, 7, 11, 6]]
print(shortestFareRoute(start2, end2, bridges2))  # Output: 10
