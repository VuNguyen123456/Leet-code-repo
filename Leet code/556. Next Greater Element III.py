# Permutation solution
class Solution(object):
  def nextGreaterElement(self, n):
      """
      :type n: int
      :rtype: int
      """
      digits = list(str(n))
      # 1. Find the first decreasing digit from the right (the pivot that was able to create a bigger num)
      i = len(digits) - 2 # -2 because -1 is the last digit so cannot compare them to the
      while i >= 0 and digits[i] >= digits[i + 1]:
      # We want to find i until a left digit is smaller than the right diggit
      # Trying to find the pivot point (where a larger number can be made from the number)
          i -= 1
      # 2. if i = -1 means the number is in decreaing order => cannot find larger number
      if i == -1:
          return -1
      # 3. Find smallest digit j to the right of i that's still bigger than i (currently at a digit where it's smaller than everything to the right of it) to make sure that the next permutation is minimally larger than given number
      j = len(digits) - 1
      while digits[j] <= digits[i]:
          j -= 1
      # 4. Swap pivot and the least big of the pivot:
      digits[i], digits[j] = digits[j], digits[i]

      # 5. Reverse: because after the swap the digits after index i may still be in a decending order (want smallest possible)
      digits[i + 1:] = reversed(digits[i + 1:])

      # 6. get result:
      result = int(''.join(digits))

      # 7. Check if result inside 32 bit sign integer range (if overflow return -1)
      return result if result <= 2**31 - 1 else -1