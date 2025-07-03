#Sliding Window

class Solution(object):
  def lengthOfLongestSubstring(self, s):
      """
      :type s: str
      :rtype: int
      """
      win = set()
      biggest = 0
      frontOfList = 0
      for i in range(len(s)):
          while s[i] in win:
              win.remove(s[frontOfList])
              frontOfList += 1
          win.add(s[i])
          biggest = max(len(win), biggest)
      print(win)
      return biggest
