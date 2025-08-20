# Date: 20/08/2025
# Question: 12
# Level: Easy
# Code: Python
# Question: Dynamic array

class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        if 0 <= i < self.size:
            return self.data[i]

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.data[self.size]
        
    def resize(self) -> None:
        self.capacity *= 2
        temp = [None] * self.capacity
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
    
    def printElems(self):
        return self.data[:self.size]


da = DynamicArray(7)

for i in range(0, 50, 10):
    da.pushback(i)
print(f"Elements are: {da.printElems()}")
print(f"Capacity: {da.getCapacity()}")
print(f"Size: {da.getSize()}")
print(f"Popped Elements: {da.popback()}")
print(f"Elements are: {da.printElems()}")
print(f"Capacity: {da.getCapacity()}")
print(f"Size: {da.getSize()}")
print(f"Resizing...")
print(f"Capacity: {da.getCapacity()}")
print(f"Size: {da.getSize()}")