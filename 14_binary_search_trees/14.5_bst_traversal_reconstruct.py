class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

# O(n), O(1)
def bst_pre_reconstruct(preorder):
   # For use as global variable
   pos = [0]
   def construct(lower, upper):
      if pos[0] == len(preorder):
         return None
      
      val = preorder[pos[0]]
      if lower <= val <= upper:
         pos[0] += 1
         left = construct(lower, val)
         right = construct(val, upper)
         return TreeNode(val, left, right)

   return construct(float('-inf'), float('inf'))
   
# O(n). O(1)
def bst_post_reconstruct(postorder):
   pos = [-1]
   def construct(lower, upper):
      if pos[0] == -1:
         return None
      
      val = postorder[pos[-1]]
      if lower <= val <= upper:
         pos[0] -= 1
         right = construct(val, upper)
         left = construct(lower, val)
         return TreeNode(val, left, right)

   return construct(float('-inf'), float('inf'))