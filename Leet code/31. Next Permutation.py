class Solution(object):
  def nextPermutation(self, nums):
      """
      :type nums: List[int]
      :rtype: None Do not return anything, modify nums in-place instead.
      """
      # 1.Find pivot
      i = len(nums) - 2
      while i >= 0 and not (nums[i] < nums[i+1]): # want nums[i] < nums[i+1]
          i -= 1

      if i == -1:
          # Handle this case by finding the smallest possible nums by sorting
          return nums.sort()
      # Find smallest j but still bigger than i
      j = len(nums) - 1
      while not (nums[j] > nums[i]): # want nums[j] < nums[i]
          j -= 1
      # Swap them
      nums[i], nums[j]  = nums[j], nums[i]

      # Reverse the stuff after pivot becasue they are deccending wto accending for smallest possible bigger
      # nums[pivot+1:] = reversed(nums[pivot+1:])
      nums[i+1:] = reversed(nums[i+1:])

      return nums