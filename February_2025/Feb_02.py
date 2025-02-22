from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0  # Count of decreasing points
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check decreasing point
                count += 1
                if count > 1:  # More than one decreasing point → Not valid
                    return False

        return True  # If only one or no decreasing point, return True
