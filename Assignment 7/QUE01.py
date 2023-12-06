from typing import List

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


print(specialHub(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))  # Output: 3


print(specialHub(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))  # Output: 0
