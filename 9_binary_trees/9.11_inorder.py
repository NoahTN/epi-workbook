# https://leetcode.com/problems/binary-tree-inorder-traversal/
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/Python-recursive-and-iterative-solutions./30044
# O(n), O(n)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        
        while stack or root:
            if root: # Simulate recursive callstack by setting target to left child
               stack.append(root)
               root = root.left
            else:    # Dead end, backtrack up stack and move to right
               node = stack.pop()
               result.append(node.val)
               root = node.right
  
        return result
            
        