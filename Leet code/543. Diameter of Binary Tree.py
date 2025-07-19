# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxDiameter = 0
        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            maxDiameter = max(maxDiameter, l + r)
            return max(l, r) + 1
        dfs(root)
        return maxDiameter