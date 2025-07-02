class Solution(object):
  def moveZeroes(self, nums):
      """
      :type nums: List[int]
      :rtype: None Do not return anything, modify nums in-place instead.
      """
      l = 0
      for r in range(len(nums)):
          # if it's not 0 swap l and r and increment both l, r (until meet a 0 both l and r are the same)
          if nums[r] != 0:
              nums[l], nums[r] = nums[r], nums[l] 
              l += 1
          # if it's 0 the ignore it because then l will be left at the index of the 0 and r will continue on until meet a non 0 to swap it's place with it
      return nums

# Adjacent zeros:
# When zeros are next to each other, the right pointer (r) skips over them without moving the left pointer (l). This means zeros stay where they are for now, and l waits for a non-zero to swap with. So multiple zeros don’t cause any issues.

# Scattered zeros:
# Since r scans every element and only swaps when it finds a non-zero, zeros spread out across the list are naturally skipped until a non-zero appears. The non-zero will be swapped forward to the position l points to, compacting all non-zeros to the front.

# No zeros:
# If there are no zeros, every element is non-zero. The r pointer swaps each element with itself or with its current position, moving l along the entire list. The array remains unchanged but is effectively “processed” correctly.
