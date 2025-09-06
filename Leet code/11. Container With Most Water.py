class Solution:
  def maxArea(self, height: List[int]) -> int:
      maxW = 0
      l = 0
      r = len(height) - 1
      while l < r:
          shorterC = min(height[l], height[r])
          curWater = (r - l) * shorterC
          maxW = max(curWater, maxW)
          if shorterC == height[l]:
              l += 1
          else:
              r -= 1
      return maxW