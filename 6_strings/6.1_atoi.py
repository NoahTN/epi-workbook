# https://leetcode.com/problems/string-to-integer-atoi/
# O(n), O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
      def clamp_result(num):
         if num < -(2**31):
               return -(2**31)
         if num > 2**31-1:
               return 2**31-1
         return num
   
      result = 0
      sign = 1
      i = 0
      # removing leading whitespace
      while i < len(s) and s[i] == ' ':
         i+=1
      
      if i == len(s):
         return 0
      
      # check for sign
      if s[i] == '+':
         i+=1
      elif s[i] == '-':
         i+=1
         sign = -1
      
      while i < len(s):
         # not a digit, exit early
         if ord(s[i]) < ord('0') or ord('9') < ord(s[i]):
            break
         # build number digit by digit
         result *= 10
         result += ord(s[i]) - ord('0')
         i+=1
      
      return clamp_result(result*sign)
        