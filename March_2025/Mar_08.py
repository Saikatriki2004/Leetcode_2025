class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Length of the string
        n = len(blocks)
        
        # Step 1: Count 'W's in the first window of size k
        count = 0
        for j in range(k):
            if blocks[j] == 'W':
                count += 1
        min_operations = count
        
        # Step 2: Slide the window from index 1 to n-k
        for i in range(1, n - k + 1):
            # Remove the contribution of the outgoing element
            if blocks[i - 1] == 'W':
                count -= 1
            # Add the contribution of the incoming element
            if blocks[i + k - 1] == 'W':
                count += 1
            # Update the minimum number of operations
            min_operations = min(min_operations, count)
        
        # Return the minimum operations needed
        return min_operations
