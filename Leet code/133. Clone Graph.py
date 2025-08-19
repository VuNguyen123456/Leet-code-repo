"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#################################################DFS
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {} # A dictionary to map old node to the new created node

        def dfs(node): # A clone function
            if node in oldToNew: # If the new node has been cloned then just return them to be able to put in the list of neighbors
                return oldToNew[node]
            copy = Node(node.val) # Clone the node (without neighbors for now)
            oldToNew[node] = copy # Map old node to new
            for neigh in node.neighbors: # Recursively clone all the neighbors and add them to the current clone's neighbors list
                copy.neighbors.append(dfs(neigh))
            return copy

        return dfs(node) if node else None


####################################################BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        #1st node: create deep copy and add it into hashmap
        oldToNew[node] = Node(node.val)

        # BFS go though every node level by level: append into queue if they are current node neighbor to check further
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                # Append nei into new Node neighbors:
                oldToNew[cur].neighbors.append(oldToNew[nei])
        return oldToNew[node]

