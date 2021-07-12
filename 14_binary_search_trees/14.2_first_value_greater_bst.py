# O(h), O(1)

def first_value_greater_bst(root, value):
   curr, first = root, None
   while curr:
      # Found node with a greater value, continue looking to left
      if curr.val > value:
         first, curr = curr, curr.left
      else:
         curr = curr.right
   return first