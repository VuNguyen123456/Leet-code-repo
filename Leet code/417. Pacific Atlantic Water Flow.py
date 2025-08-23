class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      ROWS, COLS = len(heights), len(heights[0])
      pac, alt = set(), set()

      def dfs(r, c, visited, prevH):
          if(r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevH or (r,c) in visited):
              return
          visited.add((r,c))
          dfs(r + 1, c, visited, heights[r][c])
          dfs(r - 1, c, visited, heights[r][c])
          dfs(r, c + 1, visited, heights[r][c])
          dfs(r, c - 1, visited, heights[r][c])

      # Checking the borders
      for r in range(ROWS):
          dfs(r, 0, pac, heights[r][0])
          dfs(r, COLS - 1, alt, heights[r][COLS - 1])

      for c in range(COLS):
          dfs(0, c, pac, heights[0][c])
          dfs(ROWS - 1, c, alt, heights[ROWS - 1][c])

      result = []
      for r in range(ROWS):
          for c in range(COLS):
              if (r,c) in pac and (r,c) in alt:
                  result.append([r,c])

      return result