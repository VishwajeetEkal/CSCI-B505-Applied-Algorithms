import heapq

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

# Example
hubs = [[0,0],[3,10],[2,2],[5,2],[7,0]]
print(minCostToConnectHubs(hubs))  # Output: 20
