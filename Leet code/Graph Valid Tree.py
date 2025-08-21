class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
      adj = [[] for i in range(n)]
      # Fill out adjList so that all node have their all of their connected neighbors
      for src, dst in edges:
          adj[src].append(dst)
          adj[dst].append(src)

      visited = set()
      q = deque([(0, -1)]) # [current node, parent node] # This one is 0 which is the root of the tree
      visited.add(0) # To keep track to detect circle

      while q:
          node, parent = q.popleft()
          #Check neighbor
          for nei in adj[node]:
              if parent == nei: # If neighbor of a node is parent then skip because each node have at least of of this
                  continue
              # Skipped the parent already so the parent in visit will be skipped
              # But if a neighbor of a node (exclude parent) has already been in visited => cycle => fail
              if nei in visited:
                  return False
              visited.add(nei)
              q.append((nei, node))

      # This make sure that no node is completely detach from the tree because if so that node won't be visited => not a tree
      return len(visited) == n

