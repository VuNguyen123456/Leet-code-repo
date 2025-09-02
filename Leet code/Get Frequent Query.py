from collections import defaultdict

def getFrequentQueries(threshold, timestamps, queryTypes):
    n = len(timestamps)

    # Step 1: Group timestamps by query type
    query_map = defaultdict(list)
    for t, q in zip(timestamps, queryTypes):
        query_map[q].append(t)

    result = set()

    # Step 2: For each query type, check 600-second windows
    for q, times in query_map.items():
        times.sort()  # make sure timestamps are increasing
        left = 0
        for right in range(len(times)):
            # Move left pointer until window length is <= 600
            while times[right] - times[left] > 600:
                left += 1
            # Number of queries in current window
            if right - left + 1 >= threshold:
                result.add(q)
                break  # no need to check more for this query

    return sorted(result)
