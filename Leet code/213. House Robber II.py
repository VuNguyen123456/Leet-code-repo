class Solution:
  def rob(self, nums: List[int]) -> int:
      return max(self.hr1(nums[1:]), self.hr1(nums[:-1]), nums[0])

  def hr1(self, nums):
      rob1, rob2 = 0, 0
      for i in range(len(nums)):
          temp = max(nums[i] + rob1, rob2)
          rob1 = rob2
          rob2 = temp
      return rob2