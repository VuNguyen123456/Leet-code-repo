class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
      ROWS, COLS = len(board), len(board[0])
      path = set()
      length = len(word)
      def dfs(r, c, i):
          if i == length:
              return True
          elif(r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in path or word[i] != board[r][c]):
              return False
          path.add((r,c)) # if it got pass above means it's part of the correct path at the time
          result = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
          path.remove((r,c))
          return result
      for i in range(ROWS):
          for j in range(COLS):
              if dfs(i, j, 0):
                  return True
      return False