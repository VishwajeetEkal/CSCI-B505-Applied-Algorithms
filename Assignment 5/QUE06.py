def customHeapify(arrayToHeapify):
    lengthArray = len(arrayToHeapify)

    selectElment = (lengthArray - 1) // 2
    while selectElment >= 0:
        customMaxHeapify(arrayToHeapify, selectElment, lengthArray)
        selectElment -= 1

def customMaxHeapify(arrayToHeapify, selectElment, lengthArray):
    rootElement = selectElment
    leftChild = 2 * selectElment + 1
    rightChild = 2 * selectElment + 2

    if leftChild < lengthArray and arrayToHeapify[leftChild][0] > arrayToHeapify[rootElement][0]:
        rootElement = leftChild

    if rightChild < lengthArray and arrayToHeapify[rightChild][0] > arrayToHeapify[rootElement][0]:
        rootElement = rightChild

    if rootElement != selectElment:
        arrayToHeapify[selectElment], arrayToHeapify[rootElement] = arrayToHeapify[rootElement], arrayToHeapify[selectElment]
        customMaxHeapify(arrayToHeapify, rootElement, lengthArray)

def customHeappop(arrayToHeapify):
    root = arrayToHeapify[0]
    arrayToHeapify[0] = arrayToHeapify[-1]
    arrayToHeapify.pop()
    customMaxHeapify(arrayToHeapify, 0, len(arrayToHeapify))
    return root

def customHeappush(arrayToHeapify, pushElement):
    arrayToHeapify.append(pushElement)
    selectElement = len(arrayToHeapify) - 1
    while selectElement > 0:
        parent = (selectElement - 1) // 2
        if arrayToHeapify[selectElement][0] > arrayToHeapify[parent][0]:
            arrayToHeapify[selectElement], arrayToHeapify[parent] = arrayToHeapify[parent], arrayToHeapify[selectElement]
            selectElement = parent
        else:
            break

def isRearrangePossible(s, k):
    
    magicalCountsDict = {}
    for char in s:
        if char not in magicalCountsDict:
            magicalCountsDict[char] = 1
        else:
            magicalCountsDict[char] += 1
    
    if len(magicalCountsDict) == 1:
        return False

    maxHeapMagical = [(countMagiacl, char) for char, countMagiacl in magicalCountsDict.items()]
    customHeapify(maxHeapMagical)
    
    elementsNotINHeap = []
    rearrangedString = []
    while maxHeapMagical:
        countMagical, magical = customHeappop(maxHeapMagical)
        rearrangedString.append(magical)
        elementsNotINHeap.append((countMagical-1, magical))

        if len(elementsNotINHeap) == k:
            freqMagical, char = elementsNotINHeap.pop(0)
            if freqMagical > 0:
                customHeappush(maxHeapMagical,(freqMagical, char))
    
    
    return len(rearrangedString) == len(s)
    

print(isRearrangePossible("aaabc",3))   #F
print(isRearrangePossible("aabc",3))     #T
print(isRearrangePossible("aaaabbbbcccdde",4) )      #T
print(isRearrangePossible("aaadbbcc",2))     #T
print(isRearrangePossible("aa",2) )  #F
print(isRearrangePossible("abbcdfgsdc",2))       #T
print()
print(isRearrangePossible('aabbcc', 3))  # True
print(isRearrangePossible('aaabc', 3))   # False

print(isRearrangePossible('aaadbbcc', 2))  # True
print(isRearrangePossible('aaabcc', 2))  # True
print(isRearrangePossible('aabc', 3))  # True
print(isRearrangePossible('aaaabbbbcccdde',4))  # True
print(isRearrangePossible('abbcdfgsdc', 2))  # True
print(isRearrangePossible("aa",2))
