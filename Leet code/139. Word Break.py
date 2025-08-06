class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      length = len(s)
      dp = [False] * (len(s) + 1) # Because the base case is "" and it need to be true
      dp[length] = True # Base case: "" is true
      for i in range(length - 1, -1, -1):
          for word in wordDict:
              if len(word) <= (length - i) and s[i : i + len(word)] == word:
                  dp[i] = dp[i + len(word)] # Check the previous word before this word if that's correct or not? if not the this path is doom else it's true
              if dp[i] == True:
                  break # Get the correct word then move on
      return dp[0]