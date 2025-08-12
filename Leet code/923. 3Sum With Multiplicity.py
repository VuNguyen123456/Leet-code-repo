class Solution:
  def threeSumMulti(self, arr: List[int], target: int) -> int:
      MOD = 10**9 + 7
      arr.sort()
      result = 0
      length = len(arr)
      for i in range(length):
          l, r = i + 1, length - 1
          while l < r:
              sum = arr[i] + arr[l] + arr[r]
              if sum == target:
                  if arr[l] == arr[r]:
                      count = r - l + 1
                      result += count * (count-1) // 2 # The formula to get all unique pair of an array with count length
                      break   # To prevent infi loop since l, r is not assigned in this clause
                  else:
                      countLeft = 0
                      countRight = 0
                      valLeft = arr[l]
                      valRight = arr[r]
                      while l <= r and arr[l] == valLeft:
                          countLeft += 1
                          l += 1
                      while l <= r and arr[r] == valRight:
                          countRight += 1
                          r -= 1
                      result += countLeft * countRight
              elif sum > target:
                  r -= 1
              else:
                  l += 1
      return result % MOD
