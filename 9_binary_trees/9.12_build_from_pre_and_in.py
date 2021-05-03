# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map
# O(n), O(1), O(n+h)

class Solution:
   def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
      def build(stop):
         if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            # Recurse and stop when self is found in inorder
            root.left = build(root.val)
            # Root was found, pop off
            inorder.pop()
            # Recurse and stop when parent is found in inorder
            root.right = build(stop)
            return root
      # For O(1) popping
      preorder.reverse()
      inorder.reverse()
      return build(None)