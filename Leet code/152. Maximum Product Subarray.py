class Solution:
  def maxProduct(self, nums: List[int]) -> int:
      result = max(nums)
      curMax = 1
      curMin = 1
      for i in range(len(nums)):
          temp = curMax
          curMax = max(curMax * nums[i], curMin * nums[i], nums[i])
          curMin = min(temp * nums[i], curMin * nums[i], nums[i])
          result = max(result, curMax)
      return result