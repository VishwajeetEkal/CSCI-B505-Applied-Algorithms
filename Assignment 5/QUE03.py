import heapq as hp

def findMedianPrice(prices, k):
    pricesLength = len(prices)
    answerMedianArray = []
    maxPricesHeap, minPricesHeap = [], []        
    iterPrice = 0

    while iterPrice < pricesLength:
        if not maxPricesHeap or prices[iterPrice] <= -maxPricesHeap[0]:
            hp.heappush(maxPricesHeap, -prices[iterPrice])
        else:
            hp.heappush(minPricesHeap, prices[iterPrice])
               

        while len(maxPricesHeap) > len(minPricesHeap):
            hp.heappush(minPricesHeap, -hp.heappop(maxPricesHeap))
        while len(maxPricesHeap) < len(minPricesHeap):
            hp.heappush(maxPricesHeap, -hp.heappop(minPricesHeap))


        if iterPrice >= k - 1:
            if k % 2 == 1:
                answerMedianArray.append(-maxPricesHeap[0])
            else:
                answerMedianArray.append((-maxPricesHeap[0] + minPricesHeap[0]) / 2)


            if prices[iterPrice - k + 1] <= -maxPricesHeap[0]:
                maxPricesHeap.remove(-prices[iterPrice - k + 1])
            else:
                minPricesHeap.remove(prices[iterPrice - k + 1])
        
            while len(maxPricesHeap) > len(minPricesHeap):
                hp.heappush(minPricesHeap, -hp.heappop(maxPricesHeap))
            while len(maxPricesHeap) < len(minPricesHeap):
                hp.heappush(maxPricesHeap, -hp.heappop(minPricesHeap))

        iterPrice += 1

    return answerMedianArray



print(findMedianPrice(prices = [2,3,1,5,9,6], k =3))
print(findMedianPrice(prices = [2,3,1,5,9,6], k =4))