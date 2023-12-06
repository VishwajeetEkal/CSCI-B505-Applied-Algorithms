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


def solve_puzzle(root):

    max = root.val
    treasure = 1
    level = 1
    for i in range(1, get_height(root)+1):
        chest_values = printCurrentLevel(root, i, [])
        print(chest_values)
        while chest_values:
            treasure *= chest_values.pop()
        if treasure >max:
            max = treasure
            level = i
        treasure =1
    
    return level