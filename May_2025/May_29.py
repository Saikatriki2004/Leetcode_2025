class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        import collections
        
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        # 1) Build adjacency lists
        g1 = [[] for _ in range(n)]
        for u,v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        
        g2 = [[] for _ in range(m)]
        for u,v in edges2:
            g2[u].append(v)
            g2[v].append(u)
        
        # 2) BFS on tree2 to get color‐counts (parity of depth from 0)
        depth2 = [None]*m
        depth2[0] = 0
        dq = collections.deque([0])
        while dq:
            u = dq.popleft()
            for w in g2[u]:
                if depth2[w] is None:
                    depth2[w] = depth2[u] ^ 1
                    dq.append(w)
        p = sum(1 for x in depth2 if x == 0)
        q = m - p
        best2 = max(p, q)
        
        # 3) BFS on tree1 to get depth parity, and count E0
        depth1 = [None]*n
        depth1[0] = 0
        dq = collections.deque([0])
        while dq:
            u = dq.popleft()
            for w in g1[u]:
                if depth1[w] is None:
                    depth1[w] = depth1[u] ^ 1
                    dq.append(w)
        E0 = sum(1 for x in depth1 if x == 0)
        
        # 4) For each i, even‐count in tree1 = (depth1[i]==0 ? E0 : n-E0)
        answer = [0]*n
        for i in range(n):
            even1 = E0 if depth1[i] == 0 else n - E0
            answer[i] = even1 + best2
        
        return answer
