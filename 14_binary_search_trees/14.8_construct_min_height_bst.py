class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

# O(n), O(1)
def construct_min_height_bst(arr):
   def construct(i, j):
      if i >= j:
         return None
      mid = (i+j)//2
      node = TreeNode(arr[mid])
      node.left = construct(i, mid)
      node.right = construct(mid+1, j)
      return node

   return construct(0, len(arr))   
