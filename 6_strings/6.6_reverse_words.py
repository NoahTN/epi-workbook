# https://leetcode.com/problems/reverse-words-in-a-string
# O(n), O(n)
# ! Strings are immutable in Python so a space complexity O(1) is not possible

class Solution:
    def reverseWords(self, s: str) -> str:
      words = []
      start = -1

      # Loop through and get the start:end of each word
      for i in range(len(s)):
         if s[i] == ' ':
               continue
         if start == -1:
               start = i
         if i+1 == len(s) or s[i+1] == ' ':
               words.append((start, i+1))
               start = -1

      # Append each word to result in reverse order         
      result = ""
      for i in reversed(range(len(words))):
         result += s[words[i][0]: words[i][1]]
         if i > 0:
               result += ' '
               
      return result