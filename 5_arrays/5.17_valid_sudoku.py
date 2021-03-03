# https://leetcode.com/problems/valid-sudoku/
# O(n^2), O(1)

class Solution:
   def isValidSudoku(self, board: List[List[str]]) -> bool:
      return (self.isValidRow(board) and
               self.isValidCol(board) and
               self.isValidSquare(board))
   
   def isValidRow(self, board):
      for row in board:
         if not self.isValidUnit(row):
               return False
      return True
   
   def isValidCol(self, board):
      # unzip board to look at each column
      for col in zip(*board):
         if not self.isValidUnit(col):
               return False
      return True
   
   def isValidSquare(self, board):
      for i in (0, 3, 6):
         for j in (0, 3, 6):
               square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
               if not self.isValidUnit(square):
                  return False
      return True
   # ensure no duplicates with set conversion
   def isValidUnit(self, unit):
      unit = [i for i in unit if i != '.']
      return len(set(unit)) == len(unit)
