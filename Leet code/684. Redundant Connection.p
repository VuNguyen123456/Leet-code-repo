class Solution:
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    par = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(n): # Find highest parent of node, Also flatten out the tree while at it (Find n wtill it point to it self)
        if n != par[n]: # If node is not at highest parent node
            par[n] = find(par[n]) # Flatten - reassign pointing to highestparent
        return par[n] # return the highest parent (when n == par[n] because at the highest level n will point to it self so n == par[n])

    def union(n1,n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2: # Already connected and this is the redundant edge
            return False
        # If not then we add to the tree
        if rank[p1] > rank[p2]:
            par[p2] = p1 # assign so we'll flatten it out later (smaller point to bigger)
            rank[p1] += rank[p2]
        else:
            par[p1] = p2 # assign so we'll flatten it out later
            rank[p2] += rank[p1]
        return True

    for n1,n2 in edges:
        if not union(n1,n2):
            return [n1, n2]