# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        res = []
        q = deque([root])
        zigOrZag = 0
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                # level.append(node.val)
                if zigOrZag % 2 == 0:
                    level.append(node.val)
                else:
                    level.insert(0,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # if zigOrZag % 2 != 0:
            #     level.reverse()
            res.append(level)
            zigOrZag += 1
        return res
