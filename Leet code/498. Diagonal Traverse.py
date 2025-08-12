class Solution:
  def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
      if not mat:
          return []
      numRows = len(mat)
      numCols = len(mat[0])
      result = []
      # i = 0
      row = 0 # += 1 when move down, -= 1 when move up
      col = 0 # += 1 when move up, -= 1 when move down
      up = True
      while row < numRows and col < numCols:
          result.append(mat[row][col])
          #up
          if up:
              if col == numCols - 1:
                  row += 1
                  up = False
                  continue
              elif row == 0:
                  col += 1
                  up = False
                  continue
              row -= 1
              col += 1
          #down
          else:
              if row == numRows - 1:
                  col += 1
                  up = True
                  continue
              elif col == 0:
                  row += 1
                  up = True
                  continue
              row += 1
              col -= 1
      return result 