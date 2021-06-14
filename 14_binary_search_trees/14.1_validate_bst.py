# https://leetcode.com/problems/validate-binary-search-tree
# O(n), O(n)

class Solution:
   def isValidBST(self, root: TreeNode) -> bool:
      if not root:
         return True
      stack = []
      pre = None
      
      while root or stack:
         while root:
            stack.append(root)
            root = root.left
         root = stack.pop()
         if pre and root.val <= pre.val:
            return False
         pre = root
         root = root.right
      return True