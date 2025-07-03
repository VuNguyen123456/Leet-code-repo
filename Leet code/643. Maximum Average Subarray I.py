#Sliding Window
class Solution(object):
  def findMaxAverage(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: float
      """
      if not nums:
          return 0
      winSum = 0
      SumCurr = 0
      result = nums[0]
      for i in range(len(nums)):
          if i < k:
              SumCurr += nums[i]
              result = SumCurr
              winSum = SumCurr
          else:
              winSum = winSum + nums[i] - nums[i - k]
              result = max(result, winSum)
      return float(result)/k
