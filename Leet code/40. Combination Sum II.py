class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      result = []
      candidates.sort()
      def dfs(i , curList, total):
          if total == target:
              result.append(curList.copy())
              return
          if total > target or i >= len(candidates):
              return
          curList.append(candidates[i])
          dfs(i + 1, curList, total + candidates[i])
          curList.pop()
          while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
              i += 1
          dfs(i+1,curList, total)
      dfs(0, [], 0)
      return result