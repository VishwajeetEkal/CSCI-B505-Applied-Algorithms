import heapq
def solvePuzzle(numbers):
    answerPuzzle = 0
    numbersHeap = []
    numberIter = 0
    while numberIter < len(numbers):
        numbersHeap.append([numbers[numberIter], numberIter])
        numberIter += 1
    mark = []
    heapq.heapify(numbersHeap)
    count = 0
    while numbersHeap:
        unmarkedItem = heapq.heappop(numbersHeap)
        if unmarkedItem[1] not in mark :
            count+=1
            answerPuzzle += unmarkedItem[0]
            mark.append(unmarkedItem[1])
            if unmarkedItem[1]+1 not in mark and unmarkedItem[1]+1 < len(numbers):
                mark.append(unmarkedItem[1]+1)
            if unmarkedItem[1]-1 not in mark and unmarkedItem[1]-1 >=0:                
                mark.append(unmarkedItem[1]-1)
    
    return answerPuzzle

print(solvePuzzle([2,3,5,1,3,2]))
print(solvePuzzle([2,1,3,4,5,2]))