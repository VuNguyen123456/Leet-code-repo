# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Need to set upper bound and lower bound for both left and wirte:
        # if LEFT: Upperbound is current Node (parent node) lower bound is the lower bound of parent (-infi) at the start
        # if RIGHT: Lowerbound if current Node, Upperbound is upper bound of parent (infi at the start)
        # The upperobund and lower bound of aprent is ther because in case of a zigzag grandparent thing:))
        def dfs(node, lowBound, upBound):
            if not node:
                return True
            if not (lowBound < node.val < upBound):
                return False
            return dfs(node.left, lowBound, node.val) and dfs(node.right, node.val, upBound)

        return dfs(root, float('-inf'), float('inf'))