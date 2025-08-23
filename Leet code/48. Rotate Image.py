class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
      """
      Do not return anything, modify matrix in-place instead.
      """
      l, r = 0, len(matrix) - 1 # They are index
      while l < r: # for each layer 
          for i in range(r - l): # Each side is move r - l times
              top, bot = l, r # Because this is nxn so bot, r can be the same
              topLeft = matrix[top][l + i]

              matrix[top][l + i] = matrix[bot - i][l]
              matrix[bot - i][l] = matrix[bot][r-i]
              matrix[bot][r-i] = matrix[top + i][r]
              matrix [top + i][r] = topLeft

          l += 1
          r -= 1

