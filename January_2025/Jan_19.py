import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # Add all boundary cells to the heap
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(1, n - 1):
            for i in [0, m - 1]:
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        # Directions for traversing neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        water_trapped = 0
        max_height = 0
        
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            max_height = max(max_height, height)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    water_trapped += max(0, max_height - heightMap[nx][ny])
                    heapq.heappush(min_heap, (max(heightMap[nx][ny], max_height), nx, ny))
        
        return water_trapped
