def getMinimumCost(taskCosts, operationsPerBundle, bundleCost):
    # Step 1: sort tasks descending (most expensive first)
    taskCosts.sort(reverse=True)

    n = len(taskCosts)
    price = 0
    i = 0

    # Step 2: go through tasks and buy bundles or pay individually
    while i < n:
        # Take the next group of tasks (could be fewer than operationsPerBundle)
        tasksInBundle = taskCosts[i:i + operationsPerBundle]

        # Compare cost: bundle vs sum of individual tasks
        if bundleCost < sum(tasksInBundle):
            price += bundleCost
            i += len(tasksInBundle)  # move past tasks covered by bundle
        else:
            # Remaining tasks cheaper individually → add all and finish
            price += sum(tasksInBundle)
            break

    return price
