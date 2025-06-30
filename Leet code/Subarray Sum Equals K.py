# Use prefix Sum array to solve this problem

class Solution(object):
  def subarraySum(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: int
      """
      result = 0                 # Final count of subarrays that add up to k
      curSum = 0                 # My running total as I go through the array

      prefixSums = {0: 1}        # "I've seen a sum of 0 once" — this handles cases where a subarray starts from index 0

      for n in nums:
          curSum += n            # Add the current number to my running sum

          diff = curSum - k      # What previous sum do I need to get a subarray that adds to k?, Because curSum - diff (the previous curSum) = k

          # If that needed sum (diff) has been seen before, it means
          # there's a subarray ending here that sums to k
          result += prefixSums.get(diff, 0)

          # Update how many times I've seen this curSum
          prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

      return result              # Return total count of valid subarrays
