from heapq import heappop, heappush

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        pq = [(0, 0, 0)]  # (cost, x, y)
        visited = set()

        while pq:
            cost, x, y = heappop(pq)

            if (x, y) == (m - 1, n - 1):
                return cost

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for d, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + (1 if grid[x][y] != d else 0)
                    heappush(pq, (new_cost, nx, ny))

        return -1  # Shouldn't reach here if the grid is valid.
