class Solution:
  def numDecodings(self, s: str) -> int:
      dp = {len(s): 1} # default way of making ""
      for i in range(len(s) -1, -1,-1):
          if s[i] == "0":
              dp[i] = 0
          else:
              dp[i] = dp[i+1] # Handle the case of 1 digit => how many way to decode everythng after this if it's 1 digit

          #Handle the case of 2 digit because decode can go up to max of 2 digit per letter 
          if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")): #if the current num is the not the tail (which didn't have any) thing after it and (the 2 digit start with 1 => any thing is fine after that) or (the digit start with 2 then after to the max it can have is 6 because Z is 26)
              dp[i] += dp[i+2] # The number of ways you can decode everything after the 1st 2 value after i
              # After this point we have the total way you can decode the string with digit i
      return dp[0] # The way to decode all of the string