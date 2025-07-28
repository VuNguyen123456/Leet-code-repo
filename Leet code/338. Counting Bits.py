class Solution:
  def countBits(self, n: int) -> List[int]:
      result = []
      for bitNum in range(n+1):
          count = 0
          while bitNum:
              if bitNum & 1:
                  count += 1
              bitNum >>= 1
          result.append(count)
      return result