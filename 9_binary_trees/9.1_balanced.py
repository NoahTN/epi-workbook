# https://leetcode.com/problems/balanced-binary-tree
# O(n), O(1), O(h)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
      def post_check(root):
         if root is None:
            return 0
         left  = post_check(root.left)
         right = post_check(root.right)
         # Signals that there is a height difference > 1 and will propogate up
         if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
            
         return 1 + max(left, right)
         
      return post_check(root) != -1