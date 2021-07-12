# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/discuss/274621/JavaC%2B%2BPython-Iterative-Stack-Solution
# O(n), O(n)

class Solution:
   def recoverFromPreorder(self, S: str) -> TreeNode:
      stack, i = [], 0

      while i < len(S):
         level, val = 0, ""
         # Increase depth for each dash, continue and repeat
         while i < len(S) and S[i] == '-':
            level, i = level + 1, i + 1
         # Append number to val string, continue and repeat (For multi-digit numbers)
         while i < len(S) and S[i] != '-':
            val, i = val + S[i], i + 1
         # Node is a child of a higher depth than previous, pop to reach correct depth
         while len(stack) > level:
            stack.pop()

         node = TreeNode(val)
         if stack:
            # Set node as left child is no left
            if not stack[-1].left:
               stack[-1].left = node
            # Set node as right child if left
            else: 
               stack[-1].right = node
         stack.append(node)

      return stack[0]