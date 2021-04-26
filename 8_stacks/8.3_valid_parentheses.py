# https://leetcode.com/problems/valid-parentheses
# O(n), O(1)

class Solution:
    def isValid(self, s: str) -> bool:
      close_map = {
         '}':'{',
         ']':'[',
         ')':'('
      }
      stack = []
      
      for ch in s:
         if ch in close_map:
            if not stack:
               return False
            if close_map[ch] != stack[-1]:
               return False
            stack.pop()
         else:
            stack.append(ch)
      
      return not stack