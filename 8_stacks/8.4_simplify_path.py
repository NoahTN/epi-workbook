# https://leetcode.com/problems/simplify-path/
# https://leetcode.com/problems/simplify-path/discuss/25691/9-lines-of-Python-code/24725
# O(n), O(1)

class Solution:
    def simplifyPath(self, path: str) -> str:
      stack = []
      for p in path.split("/"):
         # Move up a directory if not at root
         if p == "..":
            if stack:
               stack.pop()
         # Add directory
         elif p and p != '.':
            stack.append(p)
      # Add directories separated by '/'
      return '/' + '/'.join(stack)
            