"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [] 
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        count = 0
        maxCount = 0
        pointerStart = pointerEnd = 0
        while pointerStart < len(intervals): #Only start because we only need to know the max amount of room needed
            if start[pointerStart] < end[pointerEnd]:
                pointerStart += 1
                count += 1
            else:
                pointerEnd += 1
                count -= 1
            maxCount = max(maxCount,count)
        return maxCount
