class Solution:
  def longestPalindrome(self, s: str) -> int:
      dic = {}
      s = list(s)
      for i in range(len(s)):
          if s[i] not in dic:
              dic[s[i]] = 1
          else:
              dic[s[i]] += 1
      result = 0
      oddyet = 0
      for i in dic:
          if oddyet == 0 and dic[i] % 2 == 1:
              result += 1
              oddyet = 1
          if dic[i] > 1:
              if dic[i] % 2 == 0:
                  result += dic[i]
              else:
                  result += dic[i] - 1
      return result