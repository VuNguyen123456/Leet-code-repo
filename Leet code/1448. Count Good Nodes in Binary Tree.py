# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Go through left and right sub:
        # If that node is smaller than the current MaxValue recorded then 1 more good node is discover
        # Then change the max value recorded at that moment
        # Continue
        countGoodNode = 0
        def dfs(node, curBiggest):
            nonlocal countGoodNode
            if not node:
                return 0
            if node.val >= curBiggest:
                countGoodNode += 1
                curBiggest = node.val
            dfs(node.left, curBiggest)
            dfs(node.right, curBiggest)
        dfs(root, root.val)
        return countGoodNode