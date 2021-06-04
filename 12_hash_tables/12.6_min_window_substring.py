# https://leetcode.com/problems/minimum-window-substring/
# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
# O()
class Solution:
   def minWindow(self, s: str, t: str) -> str:
      need, missing = Counter(t), len(t)
      i = start = end = 0

      for j, ch in enumerate(s, 1):
         missing -= need[ch] > 0
         need[ch]-=1

         # Found all characters of target
         if not missing:
            # Reset occurence count of previous characters if more recently found
            while need[s[i]] < 0:
               need[s[i]] += 1
               i+=1
            # If there is not an end yet or the substring is smaller. update start and end
            if not end or j-i < end-start:
               start, end = i, j
      
      return s[start:end]