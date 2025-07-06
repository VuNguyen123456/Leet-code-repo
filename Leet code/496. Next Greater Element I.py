# Monotonic Stack solution

class Solution(object):
  def nextGreaterElement(self, nums1, nums2):
      """
      :type nums1: List[int]
      :type nums2: List[int]
      :rtype: List[int]
      """
      nums1Idx = { n:i for i, n in enumerate(nums1)} # get the index of all of the value in num1 as a list
      result = [-1] * len(nums1)

      stack = [] # Decreasing monotonic because it's find greater element: This is the stack to keep track of what element is waiting to have a greater value and filled into the result
      for i in range(len(nums2)):
          cur = nums2[i] # current Value
          while stack and cur > stack[-1]: # while the top of stack is smaller than current value
              val = stack.pop() # pop the top of stack
              index = nums1Idx[val] # get the index of that element
              result[index] = cur
          if cur in nums1Idx: # append to stack if you want the number to be added in reuslt
              stack.append(cur)
      return result