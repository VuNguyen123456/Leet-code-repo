# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root and p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) # To return the root so that it climb back up the stack and return
        elif root and p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)        
        else:
            return root