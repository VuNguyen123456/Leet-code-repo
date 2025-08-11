class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      result = []
      if not matrix:
          return result
      left, right = 0, len(matrix[0]) - 1
      top, bottom = 0, len(matrix) - 1
      while left <= right and top <= bottom:
          # 1.->
          for i in range(left, right + 1):
              result.append(matrix[top][i])
          top += 1
          # 2.down
          for i in range(top, bottom + 1):
              result.append(matrix[i][right])
          right -= 1
          # 3.<-
          if top <= bottom: # Handle when only 1 row is left and it's already added to result by (step 1), last row will always from left to right so that this one can't re go though the row from oposite again (due to top is increase and have surpass bottom => none left to check)
              for i in range(right, left -1, -1):
                  result.append(matrix[bottom][i])
              bottom -= 1
          # 4.up
          if left <= right: # Handle when only column is left which that's already covered by (step 2) due to the last colum will behandle from top down So if left > right means that the (step 2) method already run through the last column and it's already in the reuslt
              for i in range(bottom, top-1, -1):
                  result.append(matrix[i][left])
              left += 1
      return result

