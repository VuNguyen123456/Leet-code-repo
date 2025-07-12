# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        # Pre-order because we want root to leaves path so it flow from high to low
        def dfs(node, path):
            # Base case: If it's empty then don't return anything
            if not node:
                return 
            # If the path is empty (at the root currently) then add the val in path 
            if path:
                path += "->" + str(node.val)
            # If it's not the root then add the path in
            else:
                path += str(node.val)
            # Base case: if the current node doesn't have left or right => leaves node => append path and return
            if not node.left and not node.right:
                result.append(path)
                return 
            # Check root, left then check right like preorder
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, "")
        return result

