def getMinimumCost(taskCosts, operationsPerBundle, bundleCost):
  # Step 1: sort tasks descending (most expensive first)
  taskCosts.sort(reverse=True)

  n = len(taskCosts)
  price = 0
  i = 0

  # Step 2: buy bundles greedily for the most expensive remaining tasks
  while i < n:
      # Check if we have enough tasks left for a bundle
      if i + operationsPerBundle <= n:
          # Sum of tasks this bundle would cover
          bundleTasksSum = sum(taskCosts[i:i+operationsPerBundle])
          # Buy bundle only if it's cheaper than paying individually
          if bundleCost < bundleTasksSum:
              price += bundleCost
              i += operationsPerBundle  # move past tasks covered by bundle
          else:
              # Remaining tasks cheaper individually
              price += sum(taskCosts[i:])
              break
      else:
          # Less tasks left than bundle size → pay individually
          price += sum(taskCosts[i:])
          break

  return price
