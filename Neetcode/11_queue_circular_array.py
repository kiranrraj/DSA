# Date: 20/08/2025
# Question: 11
# Level: Easy
# Code: Python
# Question: Queue using Circular Array

# Attributes
    # data: fixed-size list of capacity cap
    # cap: max capacity
    # size: number of elements currently stored
    # head: index of the front element (oldest)
    # tail: index where the next element will be added

# enqueue(x)
    # Adds element at tail
    # Moves tail forward using (tail+1) % cap
    # Increases size

# dequeue()
    # Removes element at head
    # Sets that slot to None (optional, just for clarity)
    # Moves head forward using (head+1) % cap
    # Decreases size

# peek() 
    # shows the front element without removing it

# is_full / is_empty 
    # checks status

# printElems() 
    # prints the raw array backing the queue

class QueueCircularArray():
    def __init__(self, cap):
        self.data = [None] * cap
        self.cap = cap
        self.size = 0
        self.head = 0
        self.tail = 0
    
    # Add element at tail
    def enqueue(self, x):
        if self.size == self.cap:     
            print("Queue is full")
            return None
        # place new element at tail
        self.data[self.tail] = x   
        # Move tail forward by 1; wrap around using modulo
        self.tail = (self.tail + 1) % self.cap
        self.size += 1
        return True
    
    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return None
        # get value at head
        val = self.data[self.head]
        # clear the slot for clarity
        self.data[self.head] = None
        # # Move head forward by 1; wrap around using modulo
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return val

    def is_full(self):
        return self.size == self.cap

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return None if self.size == 0 else self.data[self.head]

    def printElems(self):
        return self.data


q1 = QueueCircularArray(10)

for i in range(0, 100, 10):
    q1.enqueue(i)

q1.enqueue(100)             # Queue is full condition
print(f"Print elements    : {q1.printElems()}")
print(f"Size of queue     : {q1.size}")
print(f"First element     : {q1.peek()}")
print(f"Dequeue operation : {q1.dequeue()}")
print(f"Dequeue operation : {q1.dequeue()}")
print(f"Dequeue operation : {q1.dequeue()}")
print(f"Peek the queue    : {q1.peek()}")
print(f"Print elements    : {q1.printElems()}")