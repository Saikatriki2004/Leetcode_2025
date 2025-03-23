import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Build the adjacency list for the undirected graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Initialize distances and ways
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        # Priority queue: (distance, node)
        pq = [(0, 0)]
        
        # Dijkstra's algorithm with ways counting
        while pq:
            d, u = heapq.heappop(pq)
            # Skip if a shorter path to u was already found
            if d > dist[u]:
                continue
            # Process each neighbor
            for v, time in graph[u]:
                new_dist = d + time
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_dist, v))
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n-1]
