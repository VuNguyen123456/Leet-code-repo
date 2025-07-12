# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        perLevel = 1
        result = []
        # While there's stuff left in the tree
        while q:
            eachLevel = []
            # Only pop 1 level at a time 
            for i in range(perLevel):
                node = q.popleft()
                eachLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # So that it can only pop 1 level in each for loop
            result.append(eachLevel)
            perLevel = len(q)
        # Reverse the result
        return result[::-1]