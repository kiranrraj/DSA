# Date: 19/08/2025
# Question: 11
# Level: Easy
# Code: Python
# Question: Queue using Python List

class QueueUsingList:
    def __init__(self):
        self.items = []
    
    def enqueue(self, x):
        self.items.append(x)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return None if self.is_empty() else self.items[0]
    
    def printElems(self):
        return self.items

    
q1 = QueueUsingList()
for i in range(0, 101, 10):
    q1.enqueue(i)

print(f"Print elements    : {q1.printElems()}")
print(f"Size of queue     : {q1.size()}")
print(f"First element     : {q1.peek()}")
print(f"Dequeue operation : {q1.dequeue()}")
print(f"Peek the queue    : {q1.peek()}")