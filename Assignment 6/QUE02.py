import heapq 
def cheapest_path(N, costs, start):

    costToTravel = {itr: float('inf') for itr in range(N)}
    costToTravel[start] = 0

    costPq = [(0, start)]

    while costPq:
        
        currentPrice, currentPoint = heapq.heappop(costPq)

        
        if currentPrice > costToTravel[currentPoint]:
            continue

        
        for price in enumerate(costs[currentPoint]):

            if price[1] == 0:
                continue
            newPrice = currentPrice + price[1]

            if newPrice < costToTravel[price[0]]:
                costToTravel[price[0]] = newPrice
                heapq.heappush(costPq, (newPrice, price[0]))

    return list(costToTravel.values())

print(cheapest_path( 9, [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
                         [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
                         [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ], 0 ))
print(cheapest_path(3, [ [ 0, 15, 0 ], [ 1, 0, 1 ], [ 1, 1, 0 ] ], 0))
print(cheapest_path(N = 3, start = 2, costs = [[0,50,40],[20,0,10],[60,5,0]]))