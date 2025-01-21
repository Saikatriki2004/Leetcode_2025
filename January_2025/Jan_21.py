from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Prefix sums for both rows
        top_prefix = [0] * (n + 1)  # Row 0
        bottom_prefix = [0] * (n + 1)  # Row 1
        
        for i in range(n):
            top_prefix[i + 1] = top_prefix[i] + grid[0][i]
            bottom_prefix[i + 1] = bottom_prefix[i] + grid[1][i]
        
        # The robot 1 will choose a column to minimize robot 2's maximum score
        min_second_robot_score = float('inf')
        
        for i in range(n):
            # Points left for robot 2 in the top row
            top_remaining = top_prefix[n] - top_prefix[i + 1]
            
            # Points left for robot 2 in the bottom row
            bottom_remaining = bottom_prefix[i]
            
            # Robot 2 will choose the path that gives it the maximum points
            max_points_robot_2 = max(top_remaining, bottom_remaining)
            
            # Minimize the maximum points robot 2 can collect
            min_second_robot_score = min(min_second_robot_score, max_points_robot_2)
        
        return min_second_robot_score
