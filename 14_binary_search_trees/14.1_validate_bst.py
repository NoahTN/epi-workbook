# https://leetcode.com/problems/validate-binary-search-tree
# O(n), O(n)

class Solution:
   def isValidBST(self, root: TreeNode) -> bool:
      if not root:
         return True
      stack = []
      prev = None
      
      while root or stack:
         # Iterative inorder traversal
         while root:
            stack.append(root)
            root = root.left
         root = stack.pop()
         if prev and root.val <= prev.val:
            return False
         prev = root
         root = root.right
      return True