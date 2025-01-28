class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # Base case: Out of bounds or land cell
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            # Catch fish at the current cell
            fish = grid[r][c]
            grid[r][c] = 0  # Mark the cell as visited
            
            # Explore all four directions
            fish += dfs(r + 1, c)  # Down
            fish += dfs(r - 1, c)  # Up
            fish += dfs(r, c + 1)  # Right
            fish += dfs(r, c - 1)  # Left
            
            return fish
        
        m, n = len(grid), len(grid[0])
        max_fish = 0
        
        # Iterate through all cells in the grid
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:  # Start DFS from any water cell
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish
