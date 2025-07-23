class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      result = []
      candidates.sort()
      length = len(candidates)
      def dfs (i, curCandidates, sum):
          # If total equal
          if sum == target:
              result.append(curCandidates.copy())
              return
          for i in range(i, length):
              if sum + candidates[i] > target: # Prun if bigger than target
                  return
              curCandidates.append(candidates[i])
              # total += candidates[i] # DON"T WAWNT TO CHANGE YOUR TOTAL HERE because when return you need to backtrack
              sum += candidates[i]
              dfs(i, curCandidates, sum)
              curCandidates.pop()
              sum -= candidates[i]
      dfs(0, [], 0)
      return result