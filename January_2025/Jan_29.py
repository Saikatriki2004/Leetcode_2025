from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        n = len(edges)
        parent = list(range(n + 1))  # Parent array
        rank = [0] * (n + 1)  # Rank array

        for u, v in edges:
            if not union(u, v):  # If adding this edge creates a cycle
                return [u, v]
