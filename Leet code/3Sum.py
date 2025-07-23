class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      nums.sort()
      length = len(nums)
      result = []
      for i in range(length):
          if nums[i] > 0:
              break
          if i > 0 and nums[i] == nums[i-1]:
              continue
          l = i + 1
          r = length - 1
          while l < r:
              if nums[l] + nums[r] + nums[i] == 0:
                  result.append([nums[i], nums[l], nums[r]])
                  l += 1
                  r -= 1 
                  while nums[l] == nums[l-1] and l < r:
                      l += 1
              elif nums[l] + nums[r] + nums[i] > 0:
                  r -= 1
              elif nums[l] + nums[r] + nums[i] < 0:
                  l += 1

      return result