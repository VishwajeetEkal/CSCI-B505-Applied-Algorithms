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
        
def prOrder(node, count):    
    if node== None:
        return count

    return prOrder(node.right, count+1)

def preOrder1(root, sum, sum_list):
    if not root:
        if sum not in sum_list:
            sum_list.append(sum)
        return sum_list

    sum*=10
    sum += root.value

    preOrder1(root.left, sum, sum_list)
    preOrder1(root.right,sum, sum_list)

    return sum_list

def list_oracle_nodes(root, max, count):
    if root:
        if max <= root.value:
            count.append(root.value)
            max = root.value
            
        list_oracle_nodes(root.left, max, count)
        list_oracle_nodes(root.right, max, count)
    return count
    


def get_height(current):
    if current:

        left_tree_height = get_height(current.left)
        right_tree_height = get_height(current.right)
 
        if left_tree_height > right_tree_height:
            return left_tree_height+1
        else:
            return right_tree_height+1
    
    return 0

def printCurrentLevel(root, level, chest_values):
    if root is None:
        return chest_values
    if level == 1:
        chest_values.append(root.value)
    elif level > 1:
        printCurrentLevel(root.left, level-1, chest_values)
        printCurrentLevel(root.right, level-1, chest_values)
    return chest_values
    


def create_bt_count_oracles_extract(values:list[int], k: int):

    root = make_binary_tree(values)

    oracle_node_list = list_oracle_nodes(root,float('-inf'), [])
    
    return len(oracle_node_list) >= k

def solve_puzzle(root):

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    

    max = root.value
    treasure = 1
    level = 1
    for i in range(1, get_height(root)+1):
        chest_values = printCurrentLevel(root, i, [])
        while chest_values:
            treasure *= chest_values.pop()
        if treasure >max:
            max = treasure
            level = i
        treasure =1
        
    print(preOrder1(root,0,[]))

    return level

print(create_bt_count_oracles_extract([3, 1, 4, 3, 1, 5], k = 4))
print(create_bt_count_oracles_extract([11, 10, 9, 13, 5, 14, 1], k = 4))
print(create_bt_count_oracles_extract([3,3,4,5], k = 2))