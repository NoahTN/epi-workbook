# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# O(n), O(1), O(h)
# * The original EPI problem has parent pointers

class Solution:
   def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      # Terminate at dead end or at target node
      if root in (None, p, q): 
         return root
      
      left = self.lowestCommonAncestor(root.left, p, q)
      right = self.lowestCommonAncestor(root.right, p, q)
      # Return the common ancstor
      if left and right:
         return root
      # Return the common ancestor from either path "up" the callstack
      return left or right