from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        def isValid(x, y):
            return 0 <= x < n and 0 <= y < n
        
        # Step 1: Label islands and compute their areas
        island_label = 2  # Start labeling from 2 to distinguish from 1
        area_map = {0: 0}  # Store island sizes, 0 is for water
        
        def dfs(x, y, label):
            stack = [(x, y)]
            grid[x][y] = label
            size = 1
            while stack:
                i, j = stack.pop()
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if isValid(ni, nj) and grid[ni][nj] == 1:
                        grid[ni][nj] = label
                        stack.append((ni, nj))
                        size += 1
            return size
        
        # Label each island and store its size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area_map[island_label] = dfs(i, j, island_label)
                    island_label += 1
        
        # Step 2: Find the max island size before any change
        max_size = max(area_map.values())  # Largest island already present
        
        # Step 3: Try flipping each 0 to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighboring_islands = set()
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if isValid(ni, nj) and grid[ni][nj] > 1:
                            neighboring_islands.add(grid[ni][nj])
                    
                    # Compute possible island size after flipping (sum of adjacent islands + 1)
                    new_island_size = 1 + sum(area_map[label] for label in neighboring_islands)
                    max_size = max(max_size, new_island_size)
        
        return max_size
