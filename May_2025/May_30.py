class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        # helper to walk from a start node and record dist[i] = distance to i, or inf if unreachable
        def build_dist(start):
            dist = [float('inf')] * n
            cur = start
            d = 0
            while cur != -1 and dist[cur] == float('inf'):
                dist[cur] = d
                d += 1
                cur = edges[cur]
            return dist
        
        dist1 = build_dist(node1)
        dist2 = build_dist(node2)
        
        # Find the node i minimizing max(dist1[i], dist2[i]); tie-break by smaller i
        ans = -1
        best = float('inf')
        for i in range(n):
            m = max(dist1[i], dist2[i])
            if m < best:
                best = m
                ans = i
        
        return ans
