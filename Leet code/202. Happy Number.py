class Solution(object):
  def isHappy(self, n):
      """
      :type n: int
      :rtype: bool
      """
      # Example: 19 = 1^2 + 9^2 = 82 or 228 = 2^2 + 2^2 + 8^2 = 84 
      def getTheNextNumber(num):
          sum = 0
          length = len(str(num))
          for i in range(length):
              digit = num % 10 # get the last digit of a number
              num /= 10 # Reduce the number by 1 letter
              sum += digit * digit
          return sum

      # Could use a dictionary or fast and slow pointer here:
      # if n == 1:
      #     return True
      # slow = n
      # fast = n
      # while True:
      #     slow = getTheNextNumber(slow)
      #     fast = getTheNextNumber(getTheNextNumber(fast))
      #     if fast == 1:
      #         return True
      #     elif slow == fast:
      #         return False

      # Dictionary version:
      slow = n
      store = set()
      store.add(slow)
      while True:
          slow = getTheNextNumber(slow)
          if slow == 1:
              return True
          elif slow in store: # if it's in the dictionary it means it's in a cycle
              return False
          store.add(slow) # add the new number to the dictionary
