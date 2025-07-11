class Solution(object):
  def findMin(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      l = 0
      r = len(nums) - 1
      while l < r:
          m = l + (r - l)//2
          if nums[m] > nums[r]: # This means the smallest value is still on the right side 
              l = m + 1
          else: # this mean m is smallest (if this is the case then the above will never be called again) or smallest is on the left side
              r = m
      # Exit after l = r eventually because of the termination condition of loop
      # return nums[r]
      return nums[l]