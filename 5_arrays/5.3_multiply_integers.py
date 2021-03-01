# https://leetcode.com/problems/multiply-strings/
# O(n*m), O(n+m)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
      # Edge case, quit early
      if num1 == '0' or num2 == '0':
         return '0'
      # Product is at most their lenghts combined
      result = [0]*(len(num1)+len(num2))
      # Make string representation abs()
      n1 = num1 if num1[0] != '-' else num1[1:]
      n2 = num2 if num2[0] != '-' else num2[1:]
      
      for i in reversed(range(len(n1))):
         for j in reversed(range(len(n2))):
                  # Multiply and calculate any carry
                  result[i+j+1] += int(n1[i]) * int(n2[j])
                  result[i+j] += result[i+j+1] // 10
                  result[i+j+1] %= 10
      # Delete leading 0 if needed
      result = result if result[0] != 0 else result[1:]
      result = ''.join(map(str, result))
      # Set sign
      if (num1[0] == '-') ^ (num2[0] == '-'):
         result = '-' + result
      return result