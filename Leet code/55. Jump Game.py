class Solution:
  def canJump(self, nums: List[int]) -> bool:
      goal = len(nums) - 1
      for i in range(len(nums) -1 -1, -1,-1): # Checking  previous if they can reach goal post or not?
          if i + nums[i] >= goal: # Can read => shift goal to it  
              goal = i
      return goal == 0