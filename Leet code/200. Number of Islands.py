class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
      ROWS, COLS = len(grid), len(grid[0])
      islands = 0

      def dfs(r, c):
          # Base case: return only because it doesn't have true/false it's modify existing grid
          if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
              return
          # Sink current island to prevent the loop bellow to repeat island
          grid[r][c] = "0"

          # Check current node neighbor to modify
          dfs(r + 1, c) # under
          dfs(r - 1, c) # up 
          dfs(r, c + 1) # right
          dfs(r, c - 1) # left

      for r in range(ROWS):
          for c in range(COLS):
              if grid[r][c] == "1":
                  dfs(r, c)
                  islands += 1
      return islands