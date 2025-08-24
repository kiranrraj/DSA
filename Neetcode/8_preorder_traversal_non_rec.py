# Date: 17/08/2025
# Question: 8
# Level: Easy
# Code: Python
# Question: Preorder Traversal [iterative]

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_iterative(root):
    if not root:
        return []

    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)
        # print(res)
        
        # push right first so left is processed next (LIFO)
        if node.right:
            stack.append(node.right) 
        if node.left:
            stack.append(node.left) 
    return res

if __name__ == "__main__":
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3)
    )

    print("Steps:")
    order = preorder_iterative(root)
    print("Final:")
    print(order)

    # Time Complexity: O(n) 
    # Space Complexity: O(h) (stack, where h is height of the tree.)