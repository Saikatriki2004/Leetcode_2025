import heapq
import bisect
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        heap = []
        heapq.heappush(heap, (dist[0][0], 0, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            current_max, i, j = heapq.heappop(heap)
            if current_max > dist[i][j]:
                continue
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    new_max = max(current_max, grid[ni][nj])
                    if new_max < dist[ni][nj]:
                        dist[ni][nj] = new_max
                        heapq.heappush(heap, (new_max, ni, nj))
        
        # Collect all reachable distances and sort them
        all_dist = []
        for i in range(m):
            for j in range(n):
                if dist[i][j] != INF:
                    all_dist.append(dist[i][j])
        all_dist.sort()
        
        # Process each query
        answer = []
        start_value = grid[0][0]
        for q in queries:
            if q <= start_value:
                answer.append(0)
            else:
                count = bisect.bisect_left(all_dist, q)
                answer.append(count)
        
        return answer