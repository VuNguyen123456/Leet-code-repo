class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
      dp = [amount + 1] * (amount + 1) # Dp will goes from [0...amount]
      dp[0] = 0
      #init to [amount + 1] because that's the biggest possible number of coin you can have if everything is just 1 
      for i in range(1, amount + 1): #for all dp[0 ... amount]
          for coin in coins: # each coin will be check
              if i >= coin: # If it's valid because if not valid meaning we didn't get to i value that's able to assign the dp value
                  dp[i] = min(dp[i], 1 + dp[i - coin]) # Whole loop is checking to see what's the smallest poissible num of coin possible to get to this i amount of money
      if dp[amount] != amount + 1:
          return dp[amount]
      else:
          return -1