class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
      appearMoreThan = len(nums)//3
      dic = {}
      for i in range(len(nums)):
          if nums[i] in dic:
              dic[nums[i]] += 1
          else:
              dic[nums[i]] = 1
      result = []
      for i in dic:
          if dic[i] > appearMoreThan:
              result.append(i)
      return result