# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        arr = []
        # this can sort out the tree and point it in array: accending order
        def dfs(node, arr):
            if not node:
                return
            # in - order: Will produce smallest to largest list value
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)
        dfs(root, arr)

        return arr[k-1]
