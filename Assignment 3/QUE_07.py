class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None
        

def calculate_sum(root, sum, sum_list):
    sum*=10
    sum += root.data

    if root.left:
        calculate_sum(root.left, sum, sum_list)
    elif not root.right :
        sum_list.append(sum)
    if root.right:
        calculate_sum(root.right,sum, sum_list)
    elif not root.left :
        sum_list.append(sum)

    print(sum_list)
    return sum_list

def TreeOfNumbers(root) -> int:
    
    sum = 0
    sum_list = calculate_sum(root, 0, [])
    while sum_list:
        sum+= sum_list.pop()

    return int(sum/2)


root = TreeNode(4)
root.left = TreeNode(4)
root.right = TreeNode(1)

root.left.left = TreeNode(0)
root.left.right = TreeNode(5)

root.right.left = TreeNode(3)
root.right.right = TreeNode(1)

root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(2)

root.left.right.left = TreeNode(6)


print(TreeOfNumbers(root))