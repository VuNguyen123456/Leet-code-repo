class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
      adj = [[] for i in range(n)]
      # visited = [False] * n
      visited = []
      result = 0
      # Create a adj list of the undirect graph
      for u,v in edges:
          adj[u].append(v)
          adj[v].append(u)

      def bfs(root):
          q = deque([root])
          visited.append(root)
          while q:
              node = q.popleft()
              for nei in adj[node]:
                  if nei not in visited: # Haven visit this neighbor yet (you need this so that infinite loop doesn't occur)
                      visited.append(nei)
                      q.append(nei)

      for i in range(n):
          if i not in visited:
              bfs(i)
              result += 1

      return result
