class Solution(object):
  def eraseOverlapIntervals(self, intervals):
      if len(intervals) <= 1:
          return 0

      intervals.sort(key=lambda x: x[1])  # Sort by end time

      countOverlap = 0
      last_end = intervals[0][1]

      for i in range(1, len(intervals)):
          if intervals[i][0] < last_end:
              countOverlap += 1  # overlap detected so count go up and move on 
          else:
              last_end = intervals[i][1]  # update only if non-overlapping

      return countOverlap