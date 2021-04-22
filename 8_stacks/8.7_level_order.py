# https://leetcode.com/problems/binary-tree-level-order-traversal/
# O(n), O(m)

class Solution:
   def levelOrder(self, root: TreeNode) -> List[List[int]]:
      if not root:
         return None
      level = [root]
      result = []
      
      while level:
         result.append([node.val for node in level])
         temp = []
         # Add children
         for node in level:
            temp.extend([node.left, node.right])
         # Remove None from children
         level = [branch for branch in temp if branch]
         
      return result