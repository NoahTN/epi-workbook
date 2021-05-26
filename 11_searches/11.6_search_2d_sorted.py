# https://leetcode.com/problems/search-a-2d-matrix-ii/
# O(m+n), O(1)

def searchMatrix(self, matrix, target):
   row, col = 0, len(matrix[0])-1
   # Search backward through columns to exclude ranges target can't be found in
   while row < len(matrix) and col >= 0:
      if matrix[row][col] == target:
         return True
      elif matrix[row][col] < target:
         row += 1
      else:
         col -= 1
   return False