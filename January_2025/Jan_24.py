from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        in_degree = [0] * n

        # Build reverse graph and in-degree count
        for i, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(i)
            in_degree[i] = len(neighbors)

        # Collect all terminal nodes (in-degree 0)
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        # Perform BFS to find all safe nodes
        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Collect all safe nodes in sorted order
        return [i for i in range(n) if safe[i]]
