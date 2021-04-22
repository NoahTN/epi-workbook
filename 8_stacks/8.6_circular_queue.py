# https://leetcode.com/problems/design-circular-queue
# O(1), O(1)

class MyCircularQueue:

    def __init__(self, k):
        self.size = 0
        self.max_size = k
        self.q = [0]*k
        self.head = self.tail = -1
        
    def enQueue(self, value):
        if self.isFull(): 
            return False
        if self.tail == -1: # Queue is empty
            self.head = self.tail = 0
        else:
            self.tail = (self.tail+1)%self.max_size
        self.q[self.tail] = value
        self.size += 1
        return True
        
    def deQueue(self):
        if self.isEmpty(): 
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head+1)%self.max_size
        self.size -= 1
        return True
        

    def Front(self):
        return self.q[self.head] if self.size != 0 else -1

    def Rear(self):
        return self.q[self.tail] if self.size != 0 else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size
        