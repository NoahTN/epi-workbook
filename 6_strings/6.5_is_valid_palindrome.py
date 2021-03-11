# https://leetcode.com/problems/valid-palindrome
# O(n), O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
      left, right = 0, len(s)-1
      
      while left < right:
         # Ignore non-alphanumeric characters
         if not s[left].isalnum():
               left+=1
               continue
         if not s[right].isalnum():
               right-=1
               continue
            
         # Keep case the same
         if s[left].lower() != s[right].lower():
               return False
         left+=1
         right-=1
         
      return True