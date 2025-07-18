# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, sum_of_path):
            if not node:
                return False
            sum_of_path += node.val # Add up in each path
            if not node.left and not node.right: # If leaves node then return True if = to target, false if not
                return sum_of_path == targetSum
            return dfs(node.left, sum_of_path) or dfs(node.right, sum_of_path) # Only leaves node will return True or False so if only 1 is True then the whole thing is true
        return dfs(root, 0)