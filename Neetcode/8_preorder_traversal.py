# Date: 17/08/2025
# Question: 8
# Level: Easy
# Code: Python
# Question: Tree Preorder Traversal

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
        print(result)
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