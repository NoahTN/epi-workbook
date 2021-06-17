# O(h+k), O(h)

def k_largest_bst(root, k):
   k_largest = []
   stack = []
   while (root or stack) and len(k_largest) < k:
      if root:
         stack.append(root)
         root = root.right
      else:
         node = stack.pop()
         k_largest.append(node.val)
         root = node.left
   return k_largest