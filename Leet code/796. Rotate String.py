class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
      newS = s
      for i in range(len(s)):
          if newS == goal:
              return True
          else:
              newS = newS[1:] + newS[0]
      return False