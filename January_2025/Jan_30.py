from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Construct the graph using adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Find connected components and check bipartiteness
        color = {}  # Stores color for bipartite check
        components = []  # Stores nodes in each connected component

        def is_bipartite(node):
            """ BFS to check bipartiteness and collect component nodes. """
            queue = deque([node])
            color[node] = 0  # Start coloring with 0
            component = [node]
            
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[curr]  # Flip color
                        queue.append(neighbor)
                        component.append(neighbor)
                    elif color[neighbor] == color[curr]:  # Odd-cycle detected
                        return None
            return component

        visited = set()
        for node in range(1, n + 1):
            if node not in visited:
                component = is_bipartite(node)
                if component is None:
                    return -1  # Not bipartite
                components.append(component)
                visited.update(component)

        # Step 3: Compute maximum BFS depth for each component
        def max_bfs_depth(start):
            """ BFS from a node to determine the maximum depth """
            queue = deque([start])
            visited = {start}
            depth = 0
            
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                depth += 1
            return depth

        # Step 4: Compute the total maximum groups
        max_groups = 0
        for component in components:
            max_depth = 0
            for node in component:
                max_depth = max(max_depth, max_bfs_depth(node))
            max_groups += max_depth

        return max_groups
