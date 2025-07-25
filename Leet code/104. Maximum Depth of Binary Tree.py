# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         def dfs(node):
#             if not node:
#                 return 0
#             left = dfs(node.left)
#             right = dfs(node.right)
#             return 1 + max(left, right)

#         return dfs(root)
