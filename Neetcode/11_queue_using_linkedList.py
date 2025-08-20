# Date: 20/08/2025
# Question: 11
# Level: Easy
# Code: Python
# Question: Queue using Linked List


#### Enqueue
# 1. Create a new Node(x) in memory.
# 2. If the queue is empty:
#       Make both head and tail point to this new node.
# 3. Else:
#       Link the current tail.next to the new node.
#       Move tail pointer to this new node.
# 4. Increase size.

#### Dequeue
# 1. If queue is empty, return None.
# 2. Otherwise:
#       Store head.val (front element).
#       Move head pointer to head.next.
#       If queue becomes empty (head is None), also set tail = None. !!!!
# 3. Decrease size.
# 4. Return the removed value.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, x):
        node = Node(x)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if not self.head:
            print("Queue is empty")
            return None
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return val

    def peek(self):
        return None if not self.head else self.head.val
    
    def is_empty(self):
        return self.size == 0

    def printElems(self):
        elems = []
        x = self.head
        while x is not None:
            elems.append(x.val)
            x = x.next
        return elems

q1 = QueueUsingLinkedList()

for i in range(0, 100, 10):
    q1.enqueue(i)

print(f"Print elements    : {q1.printElems()}")
print(f"Size of queue     : {q1.size}")
print(f"First element     : {q1.peek()}")
print(f"Dequeue operation : {q1.dequeue()}")
print(f"Dequeue operation : {q1.dequeue()}")
print(f"Dequeue operation : {q1.dequeue()}")
print(f"Peek the queue    : {q1.peek()}")
print(f"Print elements    : {q1.printElems()}")


# Operation	    Time Complexity	    Space Complexity	Logic Summary
# Enqueue	    O(1)	            O(1)	            Insert at tail
# Dequeue	    O(1)	            O(1)	            Remove from head
# Peek	        O(1)	            O(1)	            Read head
# is_empty	    O(1)	            O(1)	            Check size
# printElems	O(n)	            O(n)	            Traverse all nodes