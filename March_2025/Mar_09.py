class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        # Initialize sum for the first window (indices 0 to k-2)
        current_sum = 0
        for j in range(k - 1):
            if colors[j] != colors[(j + 1) % n]:
                current_sum += 1
        
        count = 0
        if current_sum == k - 1:
            count += 1
        
        # Slide the window across all n positions
        for i in range(1, n):
            # Remove the outgoing pair
            if colors[(i - 1) % n] != colors[i % n]:
                current_sum -= 1
            # Add the incoming pair
            if colors[(i + k - 2) % n] != colors[(i + k - 1) % n]:
                current_sum += 1
            if current_sum == k - 1:
                count += 1
        
        return count
