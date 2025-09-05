class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        count = {} # This is a dict with purely to count n and it's count
        freq = [[] for i in range(len(nums) + 1)] # this is the count and values list to bucketsort

        # Gett the count:
        for i in nums:
            count[i] = 1 + count.get(i, 0) # Get the num as key and it's count as val
        for n, c in count.items(): # To iterate over both key and it's value
            # Get them into freq so row is the count of ele and col is array of all telement with that count
            freq[c].append(n)

        # Get the return result
        result = []
        # Go backward because want top k not bottom k
        for i in range(len(freq) - 1, 0, -1): #Ig nore count 0
            # Get all the valu that has that amount of count
            for j in freq[i]: # index is count s othis work
                result.append(j)
                if len(result) == k:
                    return result