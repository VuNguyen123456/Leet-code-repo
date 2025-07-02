# Use 2 pointer
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            left = numbers[l]
            right = numbers[r]
            if left + right == target:
                return [l+1, r+1]
            elif left + right > target:
                r -= 1
            else:
                l += 1
        return []