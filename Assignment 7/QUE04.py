import heapq

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


prices =[[0,-1,4,1,-1],[-1,0,-1,-1,-1],[4,-1,0,-1,2],[1,-1,-1,0,3],[-1,-1,2,3,0]]
s = 0
print(cheapestRoutes(s, prices))  # Output: [0, -1, 4, 1, 4]
