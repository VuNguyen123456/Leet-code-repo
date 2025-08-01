class Solution:
  def rob(self, nums: List[int]) -> int:
      rob1 = 0
      rob2 = 0
      for i in nums:
          tmp = max(i + rob1, rob2) # Check if current mnoey is bigger or the rob this place and throw away previous money?
          rob1 = rob2
          rob2 = tmp
      return rob2