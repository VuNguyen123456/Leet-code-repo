class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
      length = len(nums)
      LIS = [1] * length
      for i in range(length -1,-1,-1):
          # Loop to compare current index to every index that came after it
          for j in range(i + 1, length):
              if nums[i] < nums[j]: # Only allow increaseing subsequence
                  LIS[i] = max(LIS[i], 1 + LIS[j])
      return max(LIS)