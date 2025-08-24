# Date: 24/08/2025
# Question: 19
# Level: Easy
# Code: Python
# Question: Tree post order Traversal (One stack)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# The logic is it must handle returning to parent nodes after 
# visiting their children. The algorithm uses the last_visited 
# pointer to determine whether to traverse a node's right subtree 
# or to visit the node itself.


def postorder_one_stack(root):
    result = []
    stack = []
    last_visited = None
    current = root

    while stack or current:
        # pushes the current node onto the stack and moves to 
        # its left child
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            # If the peek node has a right child, and that right 
            # child hasn't been visited yet (checked by 
            # last_visited != peek.right), we set current to 
            # peek.right. This allows the while loop to restart 
            # the traversal down the right subtree. The 
            # last_visited check prevents us from entering an 
            # infinite loop of traversing the right child again 
            # after we've already processed it.
            if peek.right and last_visited != peek.right:
                current = peek.right
            #  If there's no right child or the right child has 
            # already been visited (meaning its entire subtree is 
            # processed), we can finally visit the peek node. Its 
            # value is appended to the result list, and the node 
            # is popped from the stack. The last_visited pointer 
            # is updated to this node, signaling that we've just 
            # completed processing this part of the tree. This 
            # allows the parent node's logic in the next loop 
            # iteration to correctly identify that its right 
            # child (the node we just popped) has been fully 
            # visited.
            else:
                result.append(peek.val)
                last_visited = stack.pop()
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Post order  :", postorder_one_stack(root)) 