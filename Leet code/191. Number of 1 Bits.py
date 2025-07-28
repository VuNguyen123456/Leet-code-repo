class Solution:
  def hammingWeight(self, n: int) -> int:
      count = 0
      while n:
          if n & 1: # if n & 1 == 1 because only 1 & 1 = 1
              count += 1
          n = n >> 1 # rightshift
      return count