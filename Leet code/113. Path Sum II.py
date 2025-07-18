# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(node, curSum, curList):
            if not node:
                return 
            curSum += node.val
            curList.append(node.val)
            if not node.left and not node.right: # leaves:
                if curSum == targetSum:
                    result.append(list(curList))
            else:
                dfs(node.left, curSum, curList)
                dfs(node.right, curSum, curList)
            curList.pop() 

        dfs(root, 0, [])
        return result