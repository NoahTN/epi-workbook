# https://leetcode.com/problems/reverse-words-in-a-string
# O(n), O(n)
# ! Strings are immutable in Python so a space complexity O(1) is not possible

class Solution:
   def reverseWords(self, s: str) -> str:
      words = []
      i = 0
      cur = ""

      while i < len(s):
            if s[i] == ' ':
                  if cur:
                        words.append(cur)
                        cur = ""
            else:
                  cur += s[i]
            i+=1

      if cur:
            words.append(cur)

      return ' '.join(reversed(words))