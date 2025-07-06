# Monotonic stack

class Solution(object):
  def nextGreaterElements(self, nums):
      """
      :type nums: List[int]
      :rtype: List[int]
      """
      length = len(nums)
      stack = [] # Monotonic decrease (this is the index not the element )
      result = [-1] * length
      #Normal Next Greater
      for i in range(length):
          curNum = nums[i]
          while stack and nums[stack[-1]] < curNum: # current Num is bigger than top of stack => add curVal value into result since it's the correct nxt greater value
              index = stack.pop() #get the element that has a greater number to be added in
              result[index] = curNum #Added the needed value into the correct index in the result
          stack.append(i)

      if not stack:
          return result
      #All the value that's still in the stack right now is the value that have no bigger in the 1st circulation so we will goes through a 2nd one (no need to append anything now)

      for i in range(length):
          curNum = nums[i]
          while stack and nums[stack[-1]] < curNum: # current Num is bigger than top of stack => add curVal value into result since it's the correct nxt greater value
              index = stack.pop()
              result[index] = curNum
      return result