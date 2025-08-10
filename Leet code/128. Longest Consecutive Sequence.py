class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        setNums = set(nums)
        for i in setNums:
            if i-1 not in setNums: # This means that i is not the start of a consecutive string => skip
                length = 0
                val = i
                while val in setNums:
                    length += 1
                    val += 1 
                maxLength = max(maxLength, length)
        return maxLength

# You basically find all the start of a protential subsequence by checking that there's no  it- 1 value in the set. then if you found it you increment (in a loop) to see how many increment you can do = > the longest one is the correct one
