class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: bool
      """
      # Hashmap way
      # dic = {} # [val : index]
      # for i in range(len(nums)):
      #     if nums[i] not in dic:
      #         dic[nums[i]] = i
      #     else:
      #         if i - dic[nums[i]] <= k:
      #             return True
      #         else:
      #             dic[nums[i]] = i
      # return False

      #Sliding window way: abs(i - j) <= k means window size must be k (so only element in that range count)
      seenBefore = set()
      for i in range(len(nums)):
          if nums[i] in seenBefore:
              return True
          seenBefore.add(nums[i])
          if len(seenBefore) > k:
              seenBefore.remove(nums[i-k]) # remove the 1st element in the set (i is current index, k is size of window so: i - k = the 1st element in the window in the arr)
      return False
