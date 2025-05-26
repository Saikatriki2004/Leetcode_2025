class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

from collections import deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        # Build adjacency list and indegree
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        # dp[i][c] = max count of color c for any path ending at i
        dp = [[0] * 26 for _ in range(n)]
        q = deque()
        # Initialize queue and dp for nodes with indegree zero
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
            # initialize count for the node's own color
            dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_val = 0
        # Topological traversal
        while q:
            u = q.popleft()
            visited += 1
            # update result
            max_val = max(max_val, max(dp[u]))
            for v in adj[u]:
                # propagate counts
                for c in range(26):
                    # if v has same color, add 1
                    dp[v][c] = max(dp[v][c], dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0))
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        # if cycle exists
        if visited != n:
            return -1
        return max_val
    def sortedInsert(self, head, data):
        new_node = Node(data)
        # Empty list case
        if head is None:
            new_node.next = new_node
            return new_node
        curr = head
        # Find insertion point
        while True:
            # Case 1: between two nodes in sorted order
            if curr.data <= data <= curr.next.data:
                break
            # Case 2: at the boundary between max and min
            if curr.data > curr.next.data:
                if data >= curr.data or data <= curr.next.data:
                    break
            curr = curr.next
            # If full loop completed
            if curr == head:
                break
        # Insert new_node
        new_node.next = curr.next
        curr.next = new_node
        # Determine new head
        # If inserting before the current head, new_node becomes new head
        if data < head.data:
            return new_node
        return head
