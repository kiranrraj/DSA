# Date: 24/08/2025
# Question: 18
# Level: Easy
# Code: Python
# Question: Tree inorder Traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    result = []
    stack = []
    current = root

    while stack or current:
        # We first traverse as far left as possible from the 
        # current node. This is because, in an inorder traversal, 
        # we must visit all the left subtree nodes before the 
        # current node itself. We continuously push the current 
        # node onto the stack and then move to its left child. 
        # This loop effectively "saves" the path back up the tree.
        if current:
            stack.append(current)
            current = current.left
        # Once current is None, it means we've gone as far left 
        # as we can. We're now at a leaf node's left side (or a 
        # node with no left child). The node at the top of the 
        # stack is the one we need to visit next. We pop it from 
        # the stack, append its value to our result list, and 
        # then move to its right child. This is the root part of 
        # the left-root-right traversal.
        else:
            node = stack.pop()
            result.append(node.val)
            # Moving to the right child (current = node.right) is 
            # the right part of the traversal. This sets up the 
            # next iteration of the while loop, which will then 
            # begin the "Go Left" phase again, but this time from 
            # the new current node (the right child of the 
            # previously visited node).
            current = node.right
        # This process repeats until both the stack is empty 
        # (meaning all saved paths have been explored) and 
        # current is None (meaning we're not currently on any 
        # node).
    return result 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder  :", inorder(root)) 