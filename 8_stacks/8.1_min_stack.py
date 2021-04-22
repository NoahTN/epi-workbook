# https://leetcode.com/problems/min-stack
# O(1), O(n)
class MinStack:

   def __init__(self):
      self.stack = []

   def push(self, val: int) -> None:
      mini = val
      # Store the current min value alongside actual value
      if self.stack:
         mini = min(mini, self.stack[-1][1])
      self.stack.append((val, mini))

   def pop(self) -> None:
      self.stack.pop()

   def top(self) -> int:
      return self.stack[-1][0]

   def getMin(self) -> int:
      return self.stack[-1][1]
