from typing import List
from collections import deque
import sys

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        
        # Build adjacency list for the tree.
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Compute parent and depth for each node using BFS from root (node 0)
        parent = [-1] * n
        depth = [0] * n
        q = deque([0])
        parent[0] = -1
        depth[0] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
        
        # Determine Bob's path: from bob to 0 using parent pointers.
        bob_path_set = set()
        cur = bob
        while cur != -1:
            bob_path_set.add(cur)
            cur = parent[cur]
        bob_depth = depth[bob]
        
        # We'll perform DFS from root to each leaf, accumulating net income.
        max_income = float('-inf')
        
        def dfs(u: int, income: int):
            nonlocal max_income
            # Determine income contribution at node u.
            if u in bob_path_set:
                # Bob's arrival time at u:
                t_B = bob_depth - depth[u]
                t_A = depth[u]
                if t_A < t_B:
                    # Alice arrives before Bob.
                    inc = amount[u]
                elif t_A == t_B:
                    # They arrive simultaneously.
                    inc = amount[u] // 2
                else:
                    # Bob arrives before Alice.
                    inc = 0
            else:
                inc = amount[u]
            
            new_income = income + inc
            
            # Check if u is a leaf.
            # In the tree, for u != 0, if its only adjacent node is its parent, then it's a leaf.
            if u != 0 and len(graph[u]) == 1:
                max_income = max(max_income, new_income)
            elif u == 0 and not graph[u]:
                max_income = max(max_income, new_income)
            
            # DFS to children (neighbors except parent).
            for v in graph[u]:
                if v == parent[u]:
                    continue
                dfs(v, new_income)
        
        dfs(0, 0)
        return max_income
