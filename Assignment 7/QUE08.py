import heapq

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

