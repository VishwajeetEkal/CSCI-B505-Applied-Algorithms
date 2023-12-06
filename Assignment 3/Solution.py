def who_wins(n, k):
    length = [ i for i in range(1,n+1)]
    run = len(length)
    while run !=1:
        for i in range(k-1):
            length.append(length.pop(0))
        length.pop(0)
        run = len(length)
    winner = length.pop()

    return winner


def is_movePossible(x,y,i,j):
    if x ==i and y==j:
        return True
    elif x > i or y >j:
        return False
    
    x_move = is_movePossible(x+y,y,i,j)

    y_move = is_movePossible(x,x+y,i,j)

    return x_move or y_move

def count_successful_school_commutes(home_coords, school_coords, N):
    result = 0
    for h,s in zip(home_coords, school_coords):
        x ,y = h[0], h[1]
        i ,j = s[0], s[1]
        if is_movePossible(x,y,i,j):
            result += 1
    return result

def makeNumber(length_of_number, K, cn):
        if length_of_number == 0:
            return [cn]
        answerNumbers = []
        
        if cn % 10 + K <= 9:
            answerNumbers += makeNumber(length_of_number - 1, K, cn * 10 + cn % 10 + K)
        
        if K != 0 and cn % 10 >= K:
            answerNumbers += makeNumber(length_of_number - 1, K, cn * 10 + cn % 10 - K)
        
        return answerNumbers
    
def zenthar_puzzle( N,K):
    if N <= 0 or K < 0:
        return []
    
    result = []
    i = 1
    while i <10:
        result += makeNumber(N - 1, K, i)
        i+=1

    result.sort()

    return result


def decompress(s):
    sck = []
    num = 0
    dcs = ''

    for c in s:
        if c >= '0' and c<='9':
            num = int(c)
        elif c == '(':
            sck.append((dcs, num))
            dcs = ''
            num = 0
        elif c == ')':
            dcs1, num1 = sck.pop()
            dcs = dcs1 + dcs * num1
        else:
            dcs += c

    return dcs


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def make_binary_tree(v):
    if not v:
        return None
    
    root = TreeNode(v.pop(0))
    q = [root]
    
    while v:
        temp = q.pop(0)
        left = v.pop(0)
        if left is not None:
            temp.left = TreeNode(left)
            q.append(temp.left)
        
        if v:
            right = v.pop(0)
            if right is not None:
                temp.right = TreeNode(right)
                q.append(temp.right)
    
    return root
        
def list_oracle_nodes(root, max, count):
    if root:
        if max <= root.value:
            count.append(root.value)
            max = root.value
            
        list_oracle_nodes(root.left, max, count)
        list_oracle_nodes(root.right, max, count)
    return count

def create_bt_count_oracles_extract(values:list[int], k: int):

    root = make_binary_tree(values)

    oracle_node_list = list_oracle_nodes(root,float('-inf'), [])
    
    return len(oracle_node_list) >= k


def getHeight(current):
    if current:

        left_tree_height = getHeight(current.left)
        right_tree_height = getHeight(current.right)
 
        if left_tree_height > right_tree_height:
            return left_tree_height+1
        else:
            return right_tree_height+1
    
    return 0

def printCurrentLevel(temp, tree_level, chestValues):
    if temp is None:
        return chestValues
    if tree_level == 1:
        chestValues.append(temp.val)
    elif tree_level > 1:
        printCurrentLevel(temp.left, tree_level-1, chestValues)
        printCurrentLevel(temp.right, tree_level-1, chestValues)
    return chestValues


def solve_puzzle(root):

    max = root.val
    treasure = 1
    level = 1
    for i in range(1, getHeight(root)+1):
        chest_values = printCurrentLevel(root, i, [])
        while chest_values:
            treasure *= chest_values.pop()
        if treasure >max:
            max = treasure
            level = i
        treasure = 1
    
    return level        

def calculate_sum(temp, sum, sum_list):
    sum*=10
    sum += temp.data

    if temp.left:
        calculate_sum(temp.left, sum, sum_list)
    elif not temp.right :
        sum_list.append(sum)
    if temp.right:
        calculate_sum(temp.right,sum, sum_list)
    elif not temp.left :
        sum_list.append(sum)

    print(sum_list)
    return sum_list

def TreeOfNumbers(root) -> int:
    
    sum = 0
    sum_list = calculate_sum(root, 0, [])
    while sum_list:
        sum+= sum_list.pop()

    return int(sum/2)

class amor_dict():
    def __init__(self, num_list = []):
        self.amort_dict = []
        i = 1
        while 2**i < len(num_list):
            i+=1
        self.lvl = i

        for i in range(self.lvl):
            self.amort_dict.append([])
        
        for i in num_list:
            self.insert(i)
    
    def insert(self, num):
        if not self.amort_dict[0]:
            self.amort_dict[0].append(num)
            return 
        else:
            self.amort_dict[0] = self.merge_list(self.amort_dict[0], [num])
            self.merge_list_insert(0)

    def merge_list(self,a= [], b= []) :
        i =0 
        j = 0
        temp =[]
        while i < len(a) and j < len(b):
            
            if a[i]< b[j]:
                temp.append(a[i])
                i+=1
            else:
                temp.append(b[j])
                j+=1

        while j < len(b):
            temp.append(b[j])
            j+=1
        
        while i < len(a):
            temp.append(a[i])
            i+=1

        return temp
    
    def merge_list_insert(self, curLevel):
        nexLevel = curLevel+1
        if nexLevel >= self.lvl:
            self.buildLevel()
        if not self.amort_dict[nexLevel]:
            self.amort_dict[nexLevel] = self.merge_list(self.amort_dict[nexLevel],self.amort_dict[curLevel] )
            self.amort_dict[curLevel] = []
            return  
        self.amort_dict[nexLevel] = self.merge_list(self.amort_dict[nexLevel],self.amort_dict[curLevel]  )
        self.amort_dict[curLevel] = []
        self.merge_list_insert(nexLevel)

    def buildLevel(self):
        self.amort_dict.append([])
        self.lvl+=1

    def search(self, num):
        for i in zip(self.amort_dict, range(self.lvl) ):
            if i[0] and i[0][-1] >= num and i[0][0] <=num: 
                left = 0
                right = len(i[0])
                while left <= right:
                    mid = int( ( left+right ) / 2  )
                    if i[0][mid] == num:
                        return i[1]
                    
                    elif num >i[0][mid]      :
                        left = mid +1
                        
                    else:
                        right = mid-1
                        
        return -1

    
    
    def print(self):
        result = []
        for i in range(self.lvl):
            result+=[self.amort_dict[i][:]]
        
        return result
    


