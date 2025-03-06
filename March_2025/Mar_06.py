class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Step 1: Get the size n of the grid
        n = len(grid)
        
        # Step 2: Initialize count array of size n^2 + 1, all elements set to 0
        count = [0] * (n * n + 1)
        
        # Step 3: Count occurrences of each number in the grid
        for row in grid:
            for num in row:
                count[num] += 1
        
        # Step 4: Identify the repeating number (a) and missing number (b)
        a = None  # Repeating number
        b = None  # Missing number
        for i in range(1, n * n + 1):
            if count[i] == 2:
                a = i
            elif count[i] == 0:
                b = i
        
        # Step 5: Return the result as [a, b]
        return [a, b]
