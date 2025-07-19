# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Basically left height and right heigh cannot exceed 1
        boolean = True
        def dfs(node):
            nonlocal boolean
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            if abs(leftHeight - rightHeight) >1:
                boolean = False
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return boolean