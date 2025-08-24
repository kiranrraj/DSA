# Date: 24/08/2025
# Question: 19
# Level: Easy
# Code: Python
# Question: Tree post order Traversal (Two stack)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder_two_stacks(root):
    if not root:
        return []

    stack1, stack2 = [root], []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        result.append(node.val)

    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Post order  :", postorder_two_stacks(root)) 