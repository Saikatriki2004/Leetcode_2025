class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Helper function to check if we can select at least k non-adjacent houses
        # with each house having value <= C
        def check(C):
            count = 0
            prev_selected = False
            for num in nums:
                # Select this house if we didn't select the previous one and value <= C
                if not prev_selected and num <= C:
                    count += 1
                    prev_selected = True  # Mark this house as selected
                else:
                    prev_selected = False  # Next house can be considered
            return count >= k
        
        # Binary search boundaries
        left = min(nums)   # Minimum possible capability
        right = max(nums)  # Maximum possible capability
        
        # Binary search to find the smallest C
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                # If possible with this C, try a smaller C
                right = mid
            else:
                # If not possible, need a larger C
                left = mid + 1
        
        # Left is the smallest C where check(C) is True
        return left
