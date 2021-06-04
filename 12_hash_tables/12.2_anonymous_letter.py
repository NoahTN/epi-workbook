# https://leetcode.com/problems/ransom-note/
# O(n+m), O(m)

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
   letters = {}
   for ch in magazine:
      letters[ch] = letters.get(ch, 0)+1
   for ch in ransomNote:
      if ch not in letters:
         return False
      letters[ch] -= 1
      if letters[ch] < 0:
         return False
   return True
   # return not collections.Counter(ransomNote) - collections.Counter(magazine)