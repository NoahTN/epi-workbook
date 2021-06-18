# O(n), O(1)
def bst_pre_reconstruct(preorder):
   # For use as global variable
   pos = [0]
   def construct(lower, upper):
      if pos[0] == len(preorder):
         return None
      
      root = preorder[pos[0]]
      if lower <= root <= upper:
         pos[0] += 1
         left = construct(lower, root)
         right = construct(root, upper)
         return TreeNode(root, left, right)

   return construct(float('-inf'), float('inf'))
   
# O(n). O(1)
def bst_post_reconstruct(postorder):
   pos = [-1]
   def construct(lower, upper):
      if pos[0] == -1:
         return None
      
      root = postorder[pos[-1]]
      if lower <= root <= upper:
         pos[0] -= 1
         right = construct(root, upper)
         left = construct(lower, root)
         return TreeNode(root, left, right)

   return construct(float('-inf'), float('inf'))