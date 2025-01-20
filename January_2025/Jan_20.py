from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Create mappings to track positions of numbers in the matrix
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        
        # Initialize row and column paint counters
        row_count = [0] * m
        col_count = [0] * n
        
        for i, num in enumerate(arr):
            # Find the position of the number in the matrix
            r, c = position[num]
            
            # Increment row and column counters
            row_count[r] += 1
            col_count[c] += 1
            
            # Check if row or column is fully painted
            if row_count[r] == n or col_count[c] == m:
                return i
        
        # If no row or column is fully painted (shouldn't happen given the constraints)
        return -1
