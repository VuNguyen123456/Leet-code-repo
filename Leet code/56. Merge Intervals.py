class Solution(object):
  def merge(self, intervals):
      """
      :type intervals: List[List[int]]
      :rtype: List[List[int]]
      """
      if len(intervals) < 2:
          return intervals

      intervals.sort(key=lambda x: x[0])

      result = [intervals[0]]
      for i in range(1, len(intervals)):
          current = intervals[i]
          last = result[-1]
          if last[1] >= current[0]:
              last[1] = max(last[1], current[1]) # incase last[1] bigger than current[1]
          else:
              result.append(current)
      return result