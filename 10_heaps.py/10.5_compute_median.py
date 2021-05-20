class MedianFinder:

   def __init__(self):
      self.left = [] # Max heap using negative inputs
      self.right = [] # Min Heap
      
   def addNum(self, num: int) -> None:
      # Equal lengths, add to left and pop out smallest to right
      if len(self.left) == len(self.right):
         heappush(self.right, -heappushpop(self.left, -num))
      # Add to right and pop out smallest to left
      else:
         heappush(self.left, -heappushpop(self.right, num))
         

   def findMedian(self) -> float:
      if len(self.left) != len(self.right):
         return self.right[0]
      else:
         return (-self.left[0]+self.right[0])/2