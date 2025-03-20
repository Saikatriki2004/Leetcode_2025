class DSU:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [1] * n           # Rank for union by rank
        self.AND_val = [-1] * n       # AND_val starts as all 1s (-1 in Python)

    def find(self, x):
        # Path compression: Make the root the direct parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v, w):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            # Nodes already connected; update AND_val with new edge weight
            self.AND_val[root_u] &= w
        else:
            # Merge components, prefer higher rank as new root
            if self.rank[root_u] < self.rank[root_v]:
                root_u, root_v = root_v, root_u
            self.parent[root_u] = root_v
            # New AND_val is the AND of both components and the connecting edge
            self.AND_val[root_v] = self.AND_val[root_v] & self.AND_val[root_u] & w
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_v] += 1

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        # Process all edges to build components and compute AND_val
        for u, v, w in edges:
            dsu.union(u, v, w)
        # Answer each query
        answer = []
        for s, t in query:
            if dsu.find(s) == dsu.find(t):
                answer.append(dsu.AND_val[dsu.find(s)])
            else:
                answer.append(-1)
        return answer
