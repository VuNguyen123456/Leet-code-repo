class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
      nums.sort()
      result = nums[0] + nums[1] + nums[2] 
      for i in range(len(nums) - 2):
          l = i + 1
          r = len(nums) - 1
          closet = result
          while l < r:
              sum = nums[i] + nums[l] + nums[r]
              if sum == target:
                  return sum

              if abs(sum - target) < abs(result - target): # if new is closer to target than old, update
                  result = sum

              if sum > target:
                  r -= 1
              else:
                  l += 1
      return result