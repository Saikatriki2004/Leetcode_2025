class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph
        
        # Step 2: Initialize visited array and counter
        visited = [False] * n
        count = 0
        
        # Step 3: Find all connected components using DFS
        for i in range(n):
            if not visited[i]:
                component = []
                stack = [i]  # Iterative DFS using a stack
                while stack:
                    u = stack.pop()
                    if not visited[u]:
                        visited[u] = True
                        component.append(u)
                        for v in adj[u]:
                            if not visited[v]:
                                stack.append(v)
                
                # Step 4: Check if the component is complete
                component_set = set(component)  # For O(1) lookup
                k = len(component)
                # A component is complete if every vertex has k-1 neighbors in the component
                if all(len([v for v in adj[u] if v in component_set]) == k - 1 for u in component):
                    count += 1
        
        # Step 5: Return the total count
        return count
