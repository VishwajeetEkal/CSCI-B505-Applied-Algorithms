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

        mid_val = int ( (minimumFromA + maximumFromA) / 2)

        zeroElements = []
        oneElements = []

        bitmap =""
        for element in waveletElementArray:
            if element not in self.waveletCodes: 
                self.waveletCodes[element] = ""
            
            if element <= mid_val:
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
        

wv_tree = Wavelet_Tree([6, 2, 0, 7,7,9, 3, 1, 8, 5, 4])
print(wv_tree.get_wavelet_level_order())
print(wv_tree.rank(7,3))
print(wv_tree.rank(1,9))
print(wv_tree.rank(3,7))
print(wv_tree.rank(5,1))
print(wv_tree.rank(6,1))
print(wv_tree.rank(8,0))
print(wv_tree.rank(0,2))

print("AAAAAA")
wv_tree = Wavelet_Tree([0,0,0])
print(wv_tree.get_wavelet_level_order())
print(wv_tree.rank(0,1))