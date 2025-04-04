from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        max_left = [0] * n
        for j in range(1, n):
            max_left[j] = max(max_left[j-1], nums[j-1])
        
        max_right = [0] * n
        for j in range(n-2, -1, -1):
            max_right[j] = max(max_right[j+1], nums[j+1])
        
        max_val = -float('inf')
        for j in range(1, n-1):
            current = (max_left[j] - nums[j]) * max_right[j]
            if current > max_val:
                max_val = current
        
        return max(max_val, 0)
