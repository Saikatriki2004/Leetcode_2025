from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists
        g1 = [[] for _ in range(n)]
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)

        g2 = [[] for _ in range(m)]
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        # Helper: BFS from `src` on graph `g`, up to distance `maxd`
        def bfs_count(g: List[List[int]], src: int, maxd: int) -> int:
            if maxd < 0:
                return 0
            q = deque([src])
            dist = [-1] * len(g)
            dist[src] = 0
            cnt = 1  # src itself
            while q:
                u = q.popleft()
                for w in g[u]:
                    if dist[w] == -1:
                        nd = dist[u] + 1
                        if nd > maxd:
                            continue
                        dist[w] = nd
                        cnt += 1
                        q.append(w)
            return cnt

        # 1) For each i in tree1, how many tree1-nodes are within dist <= k?
        cnt1 = [bfs_count(g1, i, k) for i in range(n)]

        # 2) In tree2, best possible count within dist <= k-1
        #    (if k == 0, you can't reach tree2 at all)
        if k == 0:
            best2 = 0
        else:
            best2 = 0
            limit2 = k - 1
            for j in range(m):
                best2 = max(best2, bfs_count(g2, j, limit2))

        # 3) answer[i] = cnt1[i] + best2
        return [cnt1[i] + best2 for i in range(n)]
