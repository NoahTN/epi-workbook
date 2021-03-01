# https://leetcode.com/problems/palindrome-number/
# Similar to reverse integer
# O(n), O(1)

class Solution:
   def isPalindrome(self, x: int) -> bool:
      if x < 0:
         return False
      
      remain, reverse = x, 0
      while remain:
         reverse = reverse*10 + remain%10
         remain //= 10
      return reverse == x