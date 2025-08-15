class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
      maxSub = nums[0] # In case of all negative
      sumA = 0 # In case of 1st value being negative
      for i in range(len(nums)):
          if sumA < 0:
              sumA = 0
          sumA += nums[i]
          maxSub = max(sumA , maxSub)
      return maxSub