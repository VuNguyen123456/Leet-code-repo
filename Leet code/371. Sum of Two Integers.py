class Solution:
  def getSum(self, a: int, b: int) -> int:
      MAX = 0x7FFFFFFF
      MASK = 0xFFFFFFFF
      while b != 0:
          tmp = a
          a = (a ^ b) & MASK
          b = ((tmp & b) << 1) & MASK
      return a if a <= MAX else ~(a^MASK)