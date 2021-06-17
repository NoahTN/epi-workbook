def compute_lca_bst(root, p, q):
   # Root is outside [p:q]
   while root.val < p.val or root.val > q.val:
      # Root is less than smallest, LCA must be in right
      while root.val < p.val:
         root = root.right
      # Root is greater than biggest, LCA must be in left
      while root.val > q.val:
         root = root.left
   return root