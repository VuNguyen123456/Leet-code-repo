class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
      # m is number of row
      # n is number of col

      # last row is all 1
      row = [1] * n # represent the last row

      for r in range(m - 1): # Skip last row bc it's all 1 
          tempRow = [1] * n # Is now the row above this (row = [1] * n)
          for ele in range(n-1-1,-1,-1): # Skipping the last col of row bc they are always 1
              tempRow[ele] = tempRow[ele+1] + row[ele] # To the left + to the down (row is the row bellow it)
          row = tempRow # Move on to the row above

      return row[0]