class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      indegree = [0] * numCourses
      adj = [[] for i in range(numCourses)] # Store all neighbor of this node

      # Init the 2 above
      for src, dst in prerequisites:
          indegree[dst] += 1 # Get this node total depend on
          adj[src].append(dst) # Get this node all it neighbor (this node doesn't have any prereq)

      q = deque()
      for i in range(numCourses):
          if indegree[i] == 0:
              q.append(i) # Get all start point of topologicall sort

      finish = 0
      while q:
          node = q.popleft()
          finish += 1
          for nei in adj[node]:
              indegree[nei] -= 1
              if indegree[nei] == 0:
                  q.append(nei)

      return finish == numCourses # If not = => there's still a node with prereq => fail