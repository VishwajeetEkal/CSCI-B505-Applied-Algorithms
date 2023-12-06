def determineStandardRadius(houses, heaters):
    heaterMaximumRadius = 0
    sortedHeaters = sorted(heaters)
    houseLength = len(houses)
    for houseItre in range(houseLength):
        leftHeaters = 0
        rightHeaters = len(sortedHeaters) - 1
        radiusReq = float('inf')

        while leftHeaters < rightHeaters:
            midpointHeater = int( (leftHeaters + rightHeaters) / 2)
            if sortedHeaters[midpointHeater] == houses[houseItre]:
                radiusReq = 0
                break
            elif sortedHeaters[midpointHeater] < houses[houseItre]:
                if abs(sortedHeaters[leftHeaters] - houses[houseItre]) < radiusReq:
                    radiusReq =  abs(sortedHeaters[midpointHeater]- houses[houseItre])
                leftHeaters = midpointHeater + 1
            else:
                if abs(sortedHeaters[leftHeaters] - houses[houseItre]) < radiusReq:
                    radiusReq =  abs(sortedHeaters[midpointHeater]- houses[houseItre])
                rightHeaters = midpointHeater

        if abs(sortedHeaters[leftHeaters] - houses[houseItre]) < radiusReq:
            radiusReq =  abs(sortedHeaters[leftHeaters]- houses[houseItre])
        
        if heaterMaximumRadius < radiusReq:
            heaterMaximumRadius = radiusReq
            
    return heaterMaximumRadius
    
