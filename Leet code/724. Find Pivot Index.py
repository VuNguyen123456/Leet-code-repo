class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
      sumArr = sum(nums)
      leftSum = 0
      for i in range(len(nums)):
          rightSum = sumArr - (leftSum + nums[i]) # right side sum = total sum - to the left and pivot index sum
          if leftSum == rightSum:
              return i
          leftSum += nums[i]
      return -1