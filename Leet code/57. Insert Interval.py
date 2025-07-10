class Solution(object):
  def insert(self, intervals, newInterval):
      """
      :type intervals: List[List[int]]
      :type newInterval: List[int]
      :rtype: List[List[int]]
      """
      if not intervals:
          return [newInterval]
      length = len(intervals)
      # O(n): because going though it is On and addng 1 more interval is also On so O(n+n) = O(n)
      for i in range(length):
          if intervals[i][0] > newInterval[0]:
              intervals.insert(i, newInterval)
              break
          elif i == length - 1:
              intervals.append(newInterval)

      # Like merge interval
      result = [intervals[0]]
      for currInterval in intervals:
          last = result[-1]
          if last[1] >= currInterval[0]:
              last[1] = max(last[1], currInterval[1])
          else:
              result.append(currInterval)
      return result