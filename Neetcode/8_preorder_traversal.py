# Date: 17/08/2025
# Question: 8
# Level: Easy
# Code: Python
# Question: Tree Preorder Traversal

# Visit the Root Node:
#   First, the function processes the current node's value.
# Traverse Left Subtree: 
#   It then makes a recursive call on the left child of the current node (dfs(node.left)). 
#   This process continues down the left side of the tree until a null node is reached.
# Traverse Right Subtree: 
#   After the left subtree has been fully traversed, the function returns to the parent and 
#   then makes a recursive call on the right child (dfs(node.right)).
# The base case is when a node is None.

# Root -> Left -> Right.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def preorder(root):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        # print(result)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result

if __name__ == "__main__":
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3)
    )
    order = preorder(root)
    print("Final:", order)