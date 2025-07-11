class Solution(object):
  def search(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: int
      """

      # Find the minimum index: it's the cut of point between 2 list
      # With Binary search
      l = 0
      r = len(nums)-1
      while l < r:
          m = l + (r - l)//2
          if nums[m] > nums[r]: # mean minimum is on the right side of this
              l = m+1
          else: # mean minimum is on the left side or it's m itself (no rotation only this will be called)
              r = m
      # exit after l = r = min
      min = l

      if min== 0: # if no rotation process normally
          l = 0
          r = len(nums) - 1
      elif target > nums[-1]: # if target is bigger than the last element in the array => it's in the left of array
          l = 0
          r = min - 1
      else: # its in the right side of the array
          l = min
          r = len(nums) - 1
      # Normal Binary search
      while l <= r:
          m = l + (r - l)//2
          if nums[m] == target:
              return m
          if nums[m] > target:
              r = m -1
          else:
              l = m + 1
      return -1