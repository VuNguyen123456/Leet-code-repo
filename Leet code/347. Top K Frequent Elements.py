class Solution(object):
  def topKFrequent(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: List[int]
      """
      # On
      dic = {}
      for i in nums:
          if i not in dic:
              dic[i] = 1
          else:
              dic[i] += 1
      # O (nlogk)
      # Add the value of dic[nums] into minheap and do as a find top k largest ele
      min_heap = []
      for i in dic:
          heapq.heappush(min_heap, [dic[i], i]) # dic[i] is the frequency: and it must be before i in this order [freq, i] because min heap is looking at the 1st element to compare 
          # push before pop
          if len(min_heap) > k: 
              heapq.heappop(min_heap)

      # min heap now contain pair of number and it's sum where the frequency is in top k

      #O(k)
      # Extract the number now:
      result = []
      for freq, num in min_heap:
          result.append(num)
      return result
      # Same as this line: return [num for freq, num in min_heap]
