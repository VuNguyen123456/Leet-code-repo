def getMaximumProfit(prices, profits):
  n = len(prices)
  max_profit = -1
  for j in range(1, n-1): # Skip the 1st and last element of array
    best_left = -1
    for i in range(j):
      if prices[i] < prices[j]:
        best_left = max(best_left, profits[i])

    best_right = -1
    for k in range(j+1, n):
      if prices[j] < prices[k]:
        best_right = max(best_right, profits[k])
    if best_left != -1 and best_right != -1:
      max_profit = max(max_profit, best_left + best_right + profits[j])
  return max_profit