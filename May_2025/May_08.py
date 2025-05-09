from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Find the minimum time to reach the bottom-right room from the top-left room.
        
        Args:
            moveTime: 2D array where moveTime[i][j] is the minimum time when you can start moving to that room
            
        Returns:
            Minimum time to reach the destination room (n-1, m-1)
        """
        n, m = len(moveTime), len(moveTime[0])
        target = (n - 1, m - 1)
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Priority queue to store (current_time, position, next_move_cost)
        # We use next_move_cost to track alternating movement costs (1s and 2s)
        pq = [(0, (0, 0), 1)]  # Start at (0,0) with time 0, next move costs 1 second
        
        # Track visited states: (position, next_move_cost)
        visited = set()
        
        while pq:
            current_time, (row, col), next_move_cost = heapq.heappop(pq)
            
            # Check if we've reached the target
            if (row, col) == target:
                return current_time
            
            # Skip if this state has been visited
            if ((row, col), next_move_cost) in visited:
                continue
            
            # Mark as visited
            visited.add(((row, col), next_move_cost))
            
            # Try all four directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is valid
                if 0 <= new_row < n and 0 <= new_col < m:
                    # Calculate the time to move to the new position
                    # We can only move when current_time >= moveTime[new_row][new_col]
                    wait_time = max(0, moveTime[new_row][new_col] - current_time)
                    new_time = current_time + wait_time + next_move_cost
                    
                    # Next move will cost alternating amount (if current is 1, next is 2 and vice versa)
                    new_move_cost = 3 - next_move_cost  # Alternates between 1 and 2
                    
                    # Add to priority queue
                    heapq.heappush(pq, (new_time, (new_row, new_col), new_move_cost))
        
        # If no path found (should not happen in this problem)
        return -1
