import copy


def translate_message(arr):
    
    arr = copy.deepcopy(arr)
    arr.sort()
    indicesDict = {}
    result = 0

    for itrArr in arr:
        result = 0
        if itrArr - 7 in indicesDict:
            result = max(result, indicesDict[itrArr - 7] + 1)

        if itrArr + 7 in indicesDict:
            result = max(result, indicesDict[itrArr + 7] + 1)

        indicesDict[itrArr] = result
    return max(indicesDict.values())+1

def find_order_size(orders):
    
    uniqueShields = set()
    symmetricPairs = 0

    for order in orders:        
        [a,b] = order
        if (b,a) in uniqueShields:
            uniqueShields.remove((b,a))
            uniqueShields.add((a,b))
            symmetricPairs +=1 
        else:
            uniqueShields.add((a,b))
  
    orderSize = len(orders) - symmetricPairs

    return orderSize


def aliveOrDead(trees, tigersWish):
    numericTreeIndices = {}

    for itr, tree in enumerate(trees):
        if tree != 'X':
            value = int(tree)
            if value not in numericTreeIndices:
                numericTreeIndices[value] = []
            numericTreeIndices[value].append(itr)

    uniqueValues = list(numericTreeIndices.keys())
    for itrUniqueValues1 in range(len(uniqueValues)):
        for itrUniqueValues2 in range(1+itrUniqueValues1, len(uniqueValues)):
            for itrUniqueValues3 in range(1+itrUniqueValues2 , len(uniqueValues)):
                valueOne, valueTwo, valueThree = uniqueValues[itrUniqueValues1], uniqueValues[itrUniqueValues2], uniqueValues[itrUniqueValues3]
                target_value = tigersWish - (valueOne + valueTwo+valueThree)
                if target_value in numericTreeIndices:

                    if itrUniqueValues1!= itrUniqueValues2 and itrUniqueValues1!= itrUniqueValues3 and itrUniqueValues2 != itrUniqueValues3:
                        return 'Alive'
    return 'Dead'

def findCircusStrings(circusString):
    def hashString(str):       
        hashValue = 0
        for char in str:
            hashValue = ord(char) + hashValue * 31 
        
        return hashValue

    obsrvdSubstrings = set()
    output = []

    for itrCirc in range(len(circusString) - 9):
        currentSubstring = circusString[itrCirc:itrCirc + 10]
        currentHash = hashString(currentSubstring)
        if currentHash in obsrvdSubstrings and currentSubstring not in output: 
            output.append(currentSubstring)
        else:
            obsrvdSubstrings.add(currentHash)

    output.sort()

    return output

print(findCircusStrings("WWWWWXXXXXWWWWWXXXXXXWWWWWYYYZZZ"))


print(findCircusStrings("WWWWWWWWWWWWW"))

print(findCircusStrings("YWYWYWYWYWYW"))
