# Use prefix Sum array to solve this problem

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.prefixSumArr = [] 
        self.prefixSumArr.append(nums[0])
        for i in range(1,len(nums)):
            self.prefixSumArr.append(self.prefixSumArr[i-1] + nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefixSumArr[right]
        else:
            return self.prefixSumArr[right] - self.prefixSumArr[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)