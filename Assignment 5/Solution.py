import heapq as hp

def busRemaining(busStation) :
    if len(busStation)==0:
        return 0

    busRemain = len(busStation)
    toCheckOverlap = busStation[0][1]
    for busIter in range(1,len(busStation)):
        if toCheckOverlap >= busStation[busIter][0]:
            busRemain-=1
            if toCheckOverlap < busStation[busIter][1]:
                toCheckOverlap = busStation[busIter][1]
        else:
            toCheckOverlap = busStation[busIter][1]

    return busRemain


def solvePuzzle(numbers):
    answerPuzzle = 0
    numbersHeap = []
    numberIter = 0
    while numberIter < len(numbers):
        numbersHeap.append([numbers[numberIter], numberIter])
        numberIter += 1
    mark = []
    hp.heapify(numbersHeap)
    count = 0
    while numbersHeap:
        unmarkedItem = hp.heappop(numbersHeap)
        if unmarkedItem[1] not in mark :
            count+=1
            answerPuzzle += unmarkedItem[0]
            mark.append(unmarkedItem[1])
            if unmarkedItem[1]+1 not in mark and unmarkedItem[1]+1 < len(numbers):
                mark.append(unmarkedItem[1]+1)
            if unmarkedItem[1]-1 not in mark and unmarkedItem[1]-1 >=0:                
                mark.append(unmarkedItem[1]-1)
    
    return answerPuzzle

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


            if prices[1+iterPrice - k ] <= -maxPricesHeap[0]:
                maxPricesHeap.remove(-prices[iterPrice - k + 1])
            else:
                minPricesHeap.remove(prices[iterPrice - k + 1])
        
            while len(maxPricesHeap) > len(minPricesHeap):
                hp.heappush(minPricesHeap, -hp.heappop(maxPricesHeap))
            while len(maxPricesHeap) < len(minPricesHeap):
                hp.heappush(maxPricesHeap, -hp.heappop(minPricesHeap))

        iterPrice += 1

    return answerMedianArray

def calculateShortBuildings(heights, answerArray):
        if len(heights) <= 1:
            return heights

        midpoint = len(heights) // 2
        lowerAnsArr = calculateShortBuildings(heights[:midpoint], answerArray)
        upperAnsArr = calculateShortBuildings(heights[midpoint:], answerArray)

        shorterBuildings = []
        iterLow, iterUp = 0, 0

        while iterLow < len(lowerAnsArr) or iterUp < len(upperAnsArr):
            if iterUp == len(upperAnsArr) or (iterLow < len(lowerAnsArr) and lowerAnsArr[iterLow] <= upperAnsArr[iterUp]):
                shorterBuildings.append(lowerAnsArr[iterLow])
                answerArray[lowerAnsArr[iterLow][1]] += iterUp
                iterLow += 1
            else:
                shorterBuildings.append(upperAnsArr[iterUp])
                iterUp += 1

        return shorterBuildings

def shorterBuildings(heights):
    heightLength= len(heights)
    answerArray = [0] * heightLength

    heights = [(heights[iterHeight], iterHeight) for iterHeight in range(0,heightLength,1)]  
    calculateShortBuildings(heights, answerArray)

    return answerArray

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


def customHeapify(arrayToHeapify):
    lengthArray = len(arrayToHeapify)

    selectElment = (lengthArray - 1) // 2
    while selectElment >= 0:
        customMaxHeapify(arrayToHeapify, selectElment, lengthArray)
        selectElment -= 1

def customMaxHeapify(arrayToHeapify, selectElment, lengthArray):
    rootElement = selectElment
    leftChild =1+ 2 * selectElment 
    rightChild = 2+ 2 * selectElment

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

class Huffman():
    def __init__(self):
        self.huffman_codes = {}
        self.source_string = ""
    
    def set_source_string(self, src_str):
        self.source_string = src_str
   
    def generate_codes(self):
        huffman_codes = {}
        characterCount = {}
        for sourceStringItr in self.source_string:
            if sourceStringItr not in characterCount:
                characterCount[sourceStringItr] = 1
                huffman_codes[sourceStringItr] = ""
            else:
                characterCount[sourceStringItr] += 1
        
        characterCountHeap = []

        for character in characterCount:
            hp.heappush(characterCountHeap,(characterCount[character],character))
        
        while len(characterCountHeap) > 1 :
            firstLowFreq, firstLowString = hp.heappop(characterCountHeap)
            secondLowFreq, secondLowString = hp.heappop(characterCountHeap)

            for itrString in firstLowString:
                huffman_codes[itrString]= '0'+huffman_codes[itrString]
            
            for itrString in secondLowString:
                huffman_codes[itrString]= '1'+huffman_codes[itrString]

            hp.heappush(characterCountHeap,(firstLowFreq+secondLowFreq, firstLowString+secondLowString))

        self.huffman_codes = huffman_codes
   
    def encode_message(self, message_to_encode):
        encoded_msg = ""
        
        for msgChar in message_to_encode:
            encoded_msg += self.huffman_codes[msgChar]

        return encoded_msg

    def decode_message(self, encoded_msg):
        decoded_msg = ""
        invertedHuffman = dict(zip(self.huffman_codes.values(), self.huffman_codes.keys()))
        currenString=''
        for msgChar in encoded_msg:
            currenString +=msgChar
            if currenString  in invertedHuffman:
                    decoded_msg += invertedHuffman[currenString]
                    currenString =''
        return decoded_msg
    
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Wavelet_Tree:
    def __init__(self, A):
        self.waveletCodes = {}
        self.root = None
        self.root = self.waveletTreeBuilder(A)
             
    def waveletTreeBuilder(self, waveletElementArray ):
        
        temp = dict.fromkeys(waveletElementArray,1)

        if not waveletElementArray:
            return None

        minimumFromA, maximumFromA = min(waveletElementArray), max(waveletElementArray)

        if minimumFromA == maximumFromA :
            occurence = ""
            for _ in range(len(waveletElementArray)):
                occurence += "X"
            if minimumFromA not in self.waveletCodes:
                self.waveletCodes[minimumFromA] = ""
            return Node(occurence)        

        compareValue = int ( (minimumFromA + maximumFromA) / 2)

        zeroElements = []
        oneElements = []

        bitmap =""
        for element in waveletElementArray:
            if element not in self.waveletCodes: 
                self.waveletCodes[element] = ""
            
            if element <= compareValue:
                zeroElements.append(element)
                bitmap+='0'
                if temp[element]:
                    self.waveletCodes[element] += "0"
                    temp[element] = 0
            else:
                oneElements.append(element)
                bitmap+='1'
                if temp[element]:
                    self.waveletCodes[element] += "1"
                    temp[element] = 0

        left_child = self.waveletTreeBuilder(zeroElements)
        right_child = self.waveletTreeBuilder(oneElements)

        return Node(bitmap, left_child, right_child)

    def get_wavelet_level_order(self):
        
        if not self.root:
            return []

        orderedWaveletTree = []
        traversalQue = [self.root]

        while traversalQue:
            traversedCur = []
            traverseNex = []

            for queIterNode in traversalQue:
                traversedCur.append(queIterNode.data)
                if queIterNode.left:
                    traverseNex.append(queIterNode.left)
                if queIterNode.right:
                    traverseNex.append(queIterNode.right)

            orderedWaveletTree.append(traversedCur)
            traversalQue = traverseNex
        
        return orderedWaveletTree

    def rank(self, element, position):
        if not self.root or element not in self.waveletCodes:
            return 0
        
        if 'X' in self.root.data :        
                return len(self.root.data[:position])
        
        return self.getRank(self.waveletCodes[element], position, self.root)
        
    def getRank(self,  elementBitcode,  index, node):
        
        if len(elementBitcode) == 0:
            return index
        
        searchBit = elementBitcode[0]

        searchBitCount = node.data[:index].count(searchBit)

        if searchBitCount == 0:
            return 0
        
        if searchBit=='1':
            return self.getRank(elementBitcode[1:], searchBitCount,  node.right )
        else:
            return self.getRank(elementBitcode[1:], searchBitCount,  node.left )


print(Wavelet_Tree([6, 2, 0, 7, 9, 3, 1, 8, 5, 4]).get_wavelet_level_order())
print(Wavelet_Tree([6, 2, 0, 7, 7, 9, 3, 1, 8, 5, 4]).get_wavelet_level_order())
print(Wavelet_Tree([6, 2, 2, 2, 0, 7, 7, 2, 9, 3, 1, 8, 5, 4]).get_wavelet_level_order())
print(Wavelet_Tree([0,0,0]).get_wavelet_level_order())
print(Wavelet_Tree([1,2,3,4,5]).get_wavelet_level_order())


print(Wavelet_Tree([6, 2, 0, 7, 9, 3, 1, 8, 5, 4]).rank(7, 3))
print(Wavelet_Tree([6, 2, 0, 7, 7, 9, 3, 1, 8, 5, 4]).rank(7, 5))
print(Wavelet_Tree([6, 2, 2, 2, 0, 7, 7, 2, 9, 3, 1, 8, 5, 4]).rank(4, 14))
print(Wavelet_Tree([0,0,0]).rank(0, 1))
print(Wavelet_Tree([1,2,3,4,5]).rank(2, 1))

