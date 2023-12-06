import heapq

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

# Example 1
n1 = 3
edges1 = [[0,1],[1,2],[0,2]]
prob1 = [0.5,0.5,0.2]
start_node1 = 0
end_node1 = 2
print(findMaxSuccessPath(n1, edges1, prob1, start_node1, end_node1))  # Output: 0.25


n2 = 3
edges2 = [[0,1]]
prob2 = [0.5]
start_node2 = 0
end_node2 = 2
print(findMaxSuccessPath(n2, edges2, prob2, start_node2, end_node2))  # Output: 0.0
